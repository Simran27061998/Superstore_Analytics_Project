# Power BI DAX Measures 

## Executive Dasboard Measures:

```DAX

1. Total Sales = SUM('superstore_sales'[sales])
2. Total Orders = DISTINCTCOUNT( superstore_sales[order_key] )
3. Total Customers = DISTINCTCOUNT( superstore_sales[customer_key] )
4. Total Shipments = COUNTROWS( superstore_sales )
5. Avg Order Value (Per Order) = DIVIDE([Total Sales], [Total Orders], 0)
6. Estimated Profit = [Total Sales]*0.25
7. Profit Margin% = DIVIDE([Estimated Profit],[Total Sales])
8. CLV – Customer Lifetime Value
       a. Avg Spend per Cust = DIVIDE( [Total Sales], [Total Customers], 0 )
       b. Orders per Cust = DIVIDE( [Total Orders], [Total Customers], 0 )
       c. CLV = [Avg Spend per Cust] * [Orders per Cust]
```

## Product Dasboard Measures:

```DAX

1. Top Category = 
VAR Tbl =
   SUMMARIZE(
    product_info,
   product_info[product_category],
    "CategorySales", CALCULATE([Total Sales])
  )
          VAR TopRow = TOPN(1, Tbl, [CategorySales], DESC)
RETURN
MAXX(TopRow, product_info[product_category])

```
```DAX

2. Top Subcategory = 
VAR Tbl =
    SUMMARIZE(
        product_info,
        product_info[product_sub_category],
        "SubSales", CALCULATE([Total Sales])
    )
VAR TopRow = TOPN(1, Tbl, [SubSales], DESC)
RETURN
MAXX(TopRow, product_info[product_sub_category])
```

```DAX

3. Avg Order Value (Per Product) = 
AVERAGEX(
    VALUES(superstore_sales[product_key]),
    CALCULATE(SUM(superstore_sales[sales]))
)
```

```DAX
 4. Pareto Visual Measures:

a. Total Sales All Selected Products(Peratto) = 
CALCULATE( [Total Sales], ALLSELECTED( product_info[product_name] ) )

b. Product Sales Rank = 
RANKX(
  ALLSELECTED( product_info[product_name] ),
  [Total Sales],
  ,
  DESC,
  DENSE
)

c. Cumulative Sales = 
VAR ThisRank = [Product Sales Rank]
RETURN
CALCULATE(
  [Total Sales],
  FILTER(
    ALLSELECTED( product_info[product_name] ),
    RANKX( ALLSELECTED( product_info[product_name] ), [Total Sales], , DESC, DENSE ) <= ThisRank
  )
)
 
d. Cumulative Sales % = 
DIVIDE( [Cumulative Sales], [Total Sales All Selected Products(Peratto)], 0 )

e. Pareto Flag (Numeric) = 
IF( [Cumulative Sales %] <= 0.8, 1, 0 )

f. Pareto Products Count = 
SUMX(
  VALUES( product_info[product_name] ),
  IF( [Cumulative Sales %] <= 0.8, 1, 0 )
)

g. Pareto Sales = 
SUMX(
  VALUES( product_info[product_name] ),
  IF( [Cumulative Sales %] <= 0.8, [Total Sales], 0 )
)

h. Pareto Sales % = 
DIVIDE( [Pareto Sales], [Total Sales All Selected Products(Peratto)], 0 )

i. Pareto Summary Text = 
VAR nProducts = [Pareto Products Count]
VAR pct = FORMAT( [Pareto Sales %], "0.0%" )
VAR totalProducts = DISTINCTCOUNT( product_info[product_name] )
RETURN
nProducts & " of " & totalProducts & " products = " & pct & " of sales (Pareto)"
```

## Customer Dashboard Measures:

```DAX
1. New Customers = 
CALCULATE(
    DISTINCTCOUNT(superstore_sales[customer_key]),
    DATEADD(Calendar[full_date], -1, YEAR)
)
```

```DAX
2. Repeat customers = 
a. Repeat Customers Count = 
COUNTROWS(
FILTER(
ADDCOLUMNS(
SUMMARIZE( superstore_sales, superstore_sales[customer_key] ),
"OrdersPerCust", CALCULATE( DISTINCTCOUNT(superstore_sales[order_key]) )
),
[OrdersPerCust] > 1
)
)
```

```DAX
b. Repeat Customer % = COALESCE( DIVIDE( [Repeat Customers Count], [Total Customers] ), 0 )
```

```DAX
3. Avg Spend per Cust = 
DIVIDE( [Total Sales], [Total Customers], 0 )
```

```DAX
4. Orders per Cust = DIVIDE( [Total Orders], [Total Customers], 0 )
```

```DAX

5. Cutsomer YOY%

a.Total Customers PY = 
VAR MinDate =
    MIN ( Calendar[full_date] )
VAR MaxDate =
    MAX ( Calendar[full_date] )
VAR ShiftMin =
    EDATE ( MinDate, -12 )   -- shift window by -12 months
VAR ShiftMax =
    EDATE ( MaxDate, -12 )
RETURN
CALCULATE(
    DISTINCTCOUNT( superstore_sales[customer_key] ),
    Calendar[full_date] >= ShiftMin &&
    Calendar[full_date] <= ShiftMax
)
```

```DAX
b. Customer YoY % = 
VAR Prev = [Total Customers PY]
VAR Curr = [Total Customers]
RETURN
IF(
    Prev = 0 || ISBLANK(Prev),
    BLANK(),
    DIVIDE( Curr - Prev, Prev )
)
```

```DAX
6. Revenue from Repeat Customers = 
CALCULATE(
    [Total Sales],
    FILTER(
        VALUES( customer_info[customer_key] ),
        CALCULATE( DISTINCTCOUNT( superstore_sales[order_key] ) ) > 1
    )
)
```

```DAX
7. Repeat Cust Rev % = 
DIVIDE( [Revenue from Repeat Customers], [Total Sales], 0 )
```

```DAX
8. Churn Rate :

a. Churn Rate = 
VAR Lost = [Lost Customers]
VAR Prev = [Prev Customers Count]
RETURN
IF( Prev = 0 || ISBLANK( Prev ), BLANK(), DIVIDE( Lost, Prev ) )
```

```DAX
b. Lost Customers = 
VAR MinDate = MIN( Calendar[full_date] )
VAR MaxDate = MAX( Calendar[full_date] )
VAR ShiftMin = EDATE( MinDate, -12 )
VAR ShiftMax = EDATE( MaxDate, -12 )

VAR CurrSet =
    CALCULATETABLE(
        VALUES( superstore_sales[customer_key] ),
        DATESBETWEEN( Calendar[full_date], MinDate, MaxDate )
    )

VAR PrevSet =
    CALCULATETABLE(
        VALUES( superstore_sales[customer_key] ),
        DATESBETWEEN( Calendar[full_date], ShiftMin, ShiftMax )
    )
```

```DAX
c. Prev Customers Count = 
VAR MinDate = MIN( Calendar[full_date] )
VAR MaxDate = MAX( Calendar[full_date] )
VAR ShiftMin = EDATE( MinDate, -12 )
VAR ShiftMax = EDATE( MaxDate, -12 )

VAR PrevSet =
    CALCULATETABLE(
        VALUES( superstore_sales[customer_key] ),
        DATESBETWEEN( Calendar[full_date], ShiftMin, ShiftMax )
    )

```

## Shipping Dashboard Measures

```
1. Late Shipments Count (Ship Date) = 
CALCULATE(
  COUNTROWS( FILTER( superstore_sales, superstore_sales[delivery_days] > 5 ) ),
  USERELATIONSHIP( date_info[date_key], superstore_sales[ship_date_key] )
)
```

```DAX
2. Late Shipments % = 
DIVIDE(
  [Late Shipments Count (Ship Date)],
  CALCULATE( COUNTROWS( superstore_sales ), USERELATIONSHIP( date_info[date_key], superstore_sales[ship_date_key] ) ),
  0
)
```

```DAX
3. On-Time Shipments% = 1 - [Late Shipments %]
```

```DAX
4. Median Delivery Days = 
CALCULATE(
  PERCENTILEX.INC(
    FILTER( superstore_sales, NOT( ISBLANK( superstore_sales[delivery_days] ) ) ),
    superstore_sales[delivery_days],
    0.5
  ),
  USERELATIONSHIP( date_info[date_key], superstore_sales[ship_date_key] )
)
```

```DAX
5. Avg Sales per Ship^ = DIVIDE( [Total Sales], [Total Shipments], 0 )
```

```DAX
6. Avg Delivery Days = 
CALCULATE(
    AVERAGE(superstore_sales[delivery_days]),
    USERELATIONSHIP(date_info[date_key], superstore_sales[ship_date_key])
) -- Using ship date
```

```DAX
7. Orders Shipped Count = 
DISTINCTCOUNT( superstore_sales[order_key] )
```

```DAX
8. Total Shipments = 
COUNTROWS( superstore_sales )
```

```DAX

9. SLA 2 Days % = 
DIVIDE(
  CALCULATE(
    COUNTROWS(superstore_sales),
    superstore_sales[delivery_days] <= 2,
    USERELATIONSHIP(date_info[date_key], superstore_sales[ship_date_key])
  ),
  CALCULATE(
    COUNTROWS(superstore_sales),
    USERELATIONSHIP(date_info[date_key], superstore_sales[ship_date_key])
  ),
  0
)
```
