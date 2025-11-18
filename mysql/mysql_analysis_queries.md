## 1. Sales Performance

## 1.1 Total Sales, Estimated Profit, Margin %, Total Orders, AOV

```sql
SELECT 
  CONCAT('$', ROUND(SUM(sales),2)) AS total_sales,
  CONCAT('$', ROUND(SUM(sales*0.25),2)) AS est_profit,
  ROUND(SUM(sales*0.25)*100 / SUM(sales), 2) AS profit_margin_percent,
  COUNT(DISTINCT order_key) AS total_orders,
  CONCAT('$', ROUND(SUM(sales)/COUNT(DISTINCT order_key),2)) AS avg_sales_per_order
FROM superstore_sales;

[Query 1.1 Output CSV](mysql_query_outputs/Total_Sales_Profitability_Orders_Overview.csv)


```

## 1.2 Sales by Year (YOY Growth %)

```sql

SELECT 
  date_info.year,
  ROUND(SUM(superstore_sales.sales),2) AS total_sales,
  ROUND(
    (SUM(superstore_sales.sales) - 
      LAG(SUM(superstore_sales.sales)) OVER (ORDER BY date_info.year))
    / LAG(SUM(superstore_sales.sales)) OVER (ORDER BY date_info.year) * 100, 
    2
  ) AS yoy_growth_percent
FROM superstore_sales
JOIN date_info ON superstore_sales.order_date_key = date_info.date_key
WHERE date_info.date_type = 'Order Date'
GROUP BY date_info.year
ORDER BY date_info.year;

```

## 1.3 Monthly Sales Trend (Seasonality)

```sql

SELECT 
  date_info.year,
  date_info.month_name,
  ROUND(SUM(superstore_sales.sales),2) AS total_sales
FROM superstore_sales 
JOIN date_info 
  ON date_info.date_key = superstore_sales.order_date_key
GROUP BY date_info.year, date_info.month_name
ORDER BY date_info.year,
         FIELD(date_info.month_name, 'January','February','March','April','May','June',
                                        'July','August','September','October','November','December');

```

 ## 1.4 Sales by Region
 
```sql

SELECT 
  region_info.region,
  ROUND(SUM(superstore_sales.sales),2) AS total_sales
FROM superstore_sales
JOIN region_info ON superstore_sales.region_key = region_info.region_key
GROUP BY region_info.region
ORDER BY total_sales DESC;

```

## 1.5 Top 10 States by Sales

```sql

SELECT 
  region_info.state,
  ROUND(SUM(superstore_sales.sales),2) AS total_sales 
FROM superstore_sales
JOIN region_info ON region_info.region_key = superstore_sales.region_key 
GROUP BY region_info.state 
ORDER BY total_sales DESC
LIMIT 10;

```
## 2. Customer Segment Insights

## 2.1 Sales & Order Count by Customer Segment

```sql

SELECT 
  customer_info.customer_segment,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales,
  COUNT(DISTINCT superstore_sales.order_key) AS total_orders,
  CONCAT('$', ROUND(SUM(superstore_sales.sales) / COUNT(DISTINCT superstore_sales.order_key),2))
      AS avg_order_value
FROM superstore_sales
JOIN customer_info ON superstore_sales.customer_key = customer_info.customer_key
GROUP BY customer_info.customer_segment
ORDER BY SUM(superstore_sales.sales) DESC;

```
## 2.2 Top 10 Customers by Sales

```sql

SELECT 
  customer_info.customer_name,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales,
  COUNT(DISTINCT superstore_sales.order_key) AS total_orders
FROM superstore_sales
JOIN customer_info ON superstore_sales.customer_key = customer_info.customer_key
GROUP BY customer_info.customer_name
ORDER BY SUM(superstore_sales.sales) DESC
LIMIT 10;

```

## 3. Product Performance
## 3.1 Sales by Product Category & Sub-Category

```sql

SELECT 
  product_info.product_category,
  product_info.product_sub_category,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN product_info ON superstore_sales.product_key = product_info.product_key
GROUP BY 
  product_info.product_category,
  product_info.product_sub_category
ORDER BY SUM(superstore_sales.sales) DESC;

```

## 3.2 Top 10 Products by Sales

```sql

SELECT 
  product_info.product_name,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN product_info ON superstore_sales.product_key = product_info.product_key
GROUP BY product_info.product_name
ORDER BY SUM(superstore_sales.sales) DESC
LIMIT 10;

```

## 3.3 Category Contribution to Total Sales

```sql

SELECT 
  product_info.product_category,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales,
  CONCAT(
      ROUND(
          SUM(superstore_sales.sales) * 100 / (SELECT SUM(sales) FROM superstore_sales),
          2
      ), '%'
  ) AS pct_of_total
FROM superstore_sales
JOIN product_info ON superstore_sales.product_key = product_info.product_key
GROUP BY product_info.product_category
ORDER BY SUM(superstore_sales.sales) DESC;

```

## 4. Shipping & Delivery Performance

## 4.1 Average Delivery Days by Ship Mode

```sql

   SELECT 
  shipping_info.ship_mode,
  ROUND(AVG(superstore_sales.delivery_days),2) AS avg_delivery_days,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN shipping_info ON superstore_sales.ship_key = shipping_info.ship_key
GROUP BY shipping_info.ship_mode
ORDER BY SUM(superstore_sales.sales) DESC;

```

## 4.2 Late vs On-Time Shipments
## Late = delivery_days > 5

```sql

SELECT
  shipping_info.ship_mode,
  CASE 
    WHEN superstore_sales.delivery_days > 5 THEN 'Late'
    ELSE 'On-Time'
  END AS delivery_status,
  COUNT(*) AS num_of_orders,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN shipping_info ON superstore_sales.ship_key = shipping_info.ship_key
GROUP BY 
  shipping_info.ship_mode,
  delivery_status
ORDER BY SUM(superstore_sales.sales) DESC;

```

## 4.3 Sales by Quarter

```sql

SELECT 
  date_info.quarter,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN date_info ON superstore_sales.order_date_key = date_info.date_key
GROUP BY quarter
ORDER BY quarter;

```

## 4.4 Delivery Days Trend by Year

```sql

SELECT 
  date_info.year,
  ROUND(AVG(superstore_sales.delivery_days),2) AS avg_delivery_days 
FROM superstore_sales
JOIN date_info ON superstore_sales.order_date_key = date_info.date_key
GROUP BY date_info.year
ORDER BY date_info.year;

```

## 5. Advanced Business Insights
## 5.1 Average Order Value Trend by Year

```sql

   SELECT 
  date_info.year,
  ROUND(
      SUM(superstore_sales.sales) / COUNT(DISTINCT superstore_sales.order_key),
      2
  ) AS avg_order_value
FROM superstore_sales
JOIN date_info ON superstore_sales.order_date_key = date_info.date_key
GROUP BY date_info.year
ORDER BY date_info.year;

```

## 5.2 Delivery Performance by Region

```sql

SELECT 
  region_info.region,
  ROUND(AVG(superstore_sales.delivery_days),2) AS avg_delivery_days,
  CONCAT('$', ROUND(SUM(superstore_sales.sales),2)) AS total_sales
FROM superstore_sales
JOIN region_info ON region_info.region_key = superstore_sales.region_key 
GROUP BY region_info.region
ORDER BY SUM(superstore_sales.sales) DESC;

```

## 5.3 Segment vs Ship Mode Preference

```sql

SELECT 
  customer_info.customer_segment,
  shipping_info.ship_mode,
  COUNT(*) AS num_of_shipments,
  ROUND(AVG(superstore_sales.delivery_days),2) AS avg_delivery_days
FROM superstore_sales
JOIN customer_info ON superstore_sales.customer_key = customer_info.customer_key
JOIN shipping_info ON superstore_sales.ship_key = shipping_info.ship_key
GROUP BY 
  customer_info.customer_segment,
  shipping_info.ship_mode
ORDER BY 
  customer_info.customer_segment,
  shipping_info.ship_mode;
```
