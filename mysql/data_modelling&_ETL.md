## 1. Source verification

```sql

SELECT * FROM superstore_cleaned LIMIT 10;

```
## 2.1 Product dimension (product_info)

```sql

create table product_info(
product_key int auto_increment primary key,
product_id varchar (100) unique not null,
product_category varchar(50) not null,
product_sub_category varchar (50) not null,
product_name varchar (200) not null);

insert ignore into  product_info ( product_id, product_category, product_sub_category, product_name) 
select distinct product_id, category, sub_category, product_name
from superstore_cleaned;
 
-- Validation checks :
 
SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT product_id) AS unique_product_ids
FROM product_info; -- The totals match

```
## 2.2 Customer dimension (customer_info)

```sql
CREATE TABLE IF NOT EXISTS customer_info(
  customer_key INT AUTO_INCREMENT PRIMARY KEY,
  customer_id VARCHAR(50) UNIQUE NOT NULL,
  customer_name VARCHAR(100) NOT NULL,
  customer_segment VARCHAR(50) NOT NULL
);

INSERT IGNORE INTO customer_info (customer_id, customer_name, customer_segment)
SELECT DISTINCT customer_id, customer_name, segment
FROM superstore_cleaned;

-- Validation checks :

SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT customer_id) AS unique_customer_ids
FROM customer_info;

```

## 2.3 Region dimension (region_info)

```sql
CREATE TABLE IF NOT EXISTS region_info(
  region_key INT AUTO_INCREMENT PRIMARY KEY,
  postal_code INT UNIQUE NOT NULL,
  region VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  city VARCHAR(50) NOT NULL
);

INSERT IGNORE INTO region_info (postal_code, region, state, city)
SELECT DISTINCT postal_code, region, state, city
FROM superstore_cleaned;

-- Validation checks :

SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT postal_code) AS unique_postal_code
FROM region_info;

```
## 2.4 Order dimension (order_info)

```sql

CREATE TABLE IF NOT EXISTS order_info(
  order_key INT AUTO_INCREMENT PRIMARY KEY,
  order_id VARCHAR(50) UNIQUE NOT NULL,
  order_date DATE NOT NULL
);

INSERT IGNORE INTO order_info (order_id, order_date)
SELECT DISTINCT order_id, order_date
FROM superstore_cleaned;

-- Validation checks :

SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT order_id) AS unique_order_ids
FROM order_info;

```

## 2.5 Shipping dimension (shipping_info)

```sql
CREATE TABLE IF NOT EXISTS shipping_info(
  ship_key INT AUTO_INCREMENT PRIMARY KEY,
  ship_date DATE NOT NULL,
  ship_mode VARCHAR(20) NOT NULL,
  UNIQUE KEY (ship_date, ship_mode)
);

INSERT IGNORE INTO shipping_info (ship_date, ship_mode)
SELECT DISTINCT ship_date, ship_mode
FROM superstore_cleaned;

-- Validation checks :

SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT ship_date, ship_mode) AS unique_date_mode_pairs
FROM shipping_info;

```
## 3.1 Date dimension (date_info)

```sql

CREATE TABLE IF NOT EXISTS date_info (
  date_key INT AUTO_INCREMENT PRIMARY KEY,
  full_date DATE NOT NULL,
  year INT NOT NULL,
  month_name VARCHAR(20) NOT NULL,
  quarter VARCHAR(20) NOT NULL,
  day_name VARCHAR(50) NOT NULL,
  type_of_day VARCHAR(50) NOT NULL,
  date_type VARCHAR(20) NOT NULL,
  UNIQUE KEY (full_date, date_type)
);

```
## 3.2 Determine min and max dates from source

```sql

SELECT 
  LEAST(
      COALESCE(MIN(order_date), '9999-12-31'),
      COALESCE(MIN(ship_date), '9999-12-31')
  ) AS min_date,
  GREATEST(
      COALESCE(MAX(order_date), '0001-01-01'),
      COALESCE(MAX(ship_date), '0001-01-01')
  ) AS max_date
FROM superstore_cleaned;


SET @min_date = (SELECT LEAST(COALESCE(MIN(order_date),'9999-12-31'), COALESCE(MIN(ship_date),'9999-12-31')) FROM superstore_cleaned);
SET @max_date = (SELECT GREATEST(COALESCE(MAX(order_date),'0001-01-01'), COALESCE(MAX(ship_date),'0001-01-01')) FROM superstore_cleaned);

```

## 3.3 Numbers table (helper) — generate 0..9999

```sql

CREATE TABLE IF NOT EXISTS numbers_0_9999 (n INT PRIMARY KEY) ENGINE=InnoDB;

INSERT IGNORE INTO numbers_0_9999 (n)
SELECT units.n + tens.n*10 + hund.n*100 + thou.n*1000 AS n
FROM
  (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) units,
  (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) tens,
  (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) hund,
  (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) thou;

--Quick Verification:

SELECT COUNT(*) AS total_numbers FROM numbers_0_9999;

```

## 3.4 Insert Order Date rows into date_info

```sql

INSERT IGNORE INTO date_info (
  full_date, year, month_name, quarter, day_name, type_of_day, date_type
)
SELECT
  cal.full_date,
  YEAR(cal.full_date)                          AS year,
  MONTHNAME(cal.full_date)                     AS month_name,
  CONCAT('Q', QUARTER(cal.full_date))          AS quarter,
  DAYNAME(cal.full_date)                       AS day_name,
  src.type_of_day,
  'Order Date'                                 AS date_type
FROM (
  SELECT DATE_ADD(@min_date, INTERVAL n DAY) AS full_date
  FROM numbers_0_9999
  WHERE DATE_ADD(@min_date, INTERVAL n DAY) BETWEEN @min_date AND @max_date
) AS cal
JOIN (
  SELECT DISTINCT DATE(order_date) AS dt, MIN(type_of_day) AS type_of_day
  FROM superstore_cleaned
  WHERE order_date IS NOT NULL
  GROUP BY DATE(order_date)
) AS src
  ON cal.full_date = src.dt
ORDER BY cal.full_date;

```

## 3.5 Insert Ship Date rows into date_info

```sql

INSERT IGNORE INTO date_info (
  full_date, year, month_name, quarter, day_name, type_of_day, date_type
)
SELECT
  sd.dt AS full_date,
  YEAR(sd.dt)                           AS year,
  MONTHNAME(sd.dt)                      AS month_name,
  CONCAT('Q', QUARTER(sd.dt))           AS quarter,
  DAYNAME(sd.dt)                        AS day_name,
  COALESCE(
      src.type_of_day,
      CASE WHEN DAYOFWEEK(sd.dt) IN (1,7) THEN 'Weekend' ELSE 'Weekday' END
  ) AS type_of_day,
  'Ship Date' AS date_type
FROM (
  SELECT DISTINCT DATE(ship_date) AS dt
  FROM superstore_cleaned
  WHERE ship_date IS NOT NULL
) sd
LEFT JOIN (
  SELECT DATE(ship_date) AS dt, MIN(type_of_day) AS type_of_day
  FROM superstore_cleaned
  WHERE ship_date IS NOT NULL AND type_of_day IS NOT NULL
  GROUP BY DATE(ship_date)
) src ON sd.dt = src.dt
ORDER BY sd.dt;

```

## 3.6 Quick inspection

```sql

SELECT * FROM date_info ORDER BY full_date, date_type LIMIT 50;

```
## 4.1 Fact table (superstore_sales)

```sql

create table superstore_sales (
product_key int not null,
customer_key int not null,
region_key int not null,
order_key int not null,
ship_key int not null,
order_date_key int not null,
ship_date_key int not null,
sales decimal(18,2), -- since float causes rounding issues
delivery_days int,
foreign key (product_key) references product_info(product_key),
foreign key (customer_key) references customer_info(customer_key),
foreign key (region_key) references region_info(region_key),
foreign key (order_key) references order_info(order_key),
foreign key (ship_key) references shipping_info(ship_key),
foreign key (order_date_key) references date_info(date_key),
foreign key (ship_date_key) references date_info(date_key));

```

## 4.2 Insert mapped rows into fact table

```sql

INSERT INTO superstore_sales (
  product_key,
  customer_key,
  region_key,
  order_key,
  ship_key,
  order_date_key,
  ship_date_key,
  sales,
  delivery_days
)
SELECT
  p.product_key,
  c.customer_key,
  r.region_key,
  o.order_key,
  s.ship_key,
  d_order.date_key AS order_date_key,
  d_ship.date_key  AS ship_date_key,
  st.sales,
  st.delivery_days
FROM superstore_cleaned st
JOIN product_info   p ON TRIM(st.product_id) = p.product_id
JOIN customer_info  c ON TRIM(st.customer_id) = c.customer_id
JOIN region_info    r ON st.postal_code = r.postal_code
JOIN order_info     o ON TRIM(st.order_id) = o.order_id
JOIN shipping_info  s ON st.ship_date = s.ship_date AND st.ship_mode = s.ship_mode
JOIN date_info d_order ON DATE(st.order_date) = d_order.full_date AND d_order.date_type = 'Order Date'
JOIN date_info d_ship  ON DATE(st.ship_date)  = d_ship.full_date  AND d_ship.date_type  = 'Ship Date';

-- Validation Check:

SELECT
  (SELECT ROUND(SUM(sales),2) FROM superstore_cleaned) AS source_sales,
  (SELECT ROUND(SUM(sales),2) FROM superstore_sales) AS fact_sales_total;

```
