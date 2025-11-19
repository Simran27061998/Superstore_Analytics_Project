# Superstore Analytics Project

End-to-end retail analytics using **Python, MySQL, and Power BI**.

---

## Project Overview

This project performs a comprehensive analysis of the Superstore dataset (2015–2018) and demonstrates a complete analytics workflow:

1. **Python** → data cleaning, feature engineering, forecasting  
2. **MySQL** → database modeling, ETL, SQL analysis  
3. **Power BI** → dashboarding and business insights  

The objective is to simulate a real-world BI/Analytics pipeline and deliver both technical and business-focused outputs.

---

## Tools & Technologies

- **Python**: Pandas, NumPy, Statsmodels, Matplotlib, SQLAlchemy  
- **MySQL**: Star schema, fact & dimension modeling, SQL queries  
- **Power BI**: Dashboards, KPIs, slicers, drill-down insights  
- **GitHub**: Version control and documentation  

---

## Repository Structure

---
Superstore_Analytics_Project/
│
├── python/
│   ├── cleaning_upload.py
│   ├── predictive_upload.py
│   └── forecast_next_7_days.csv
│
├── mysql/
│   ├── data_modelling&_ETL.md
│   ├── mysql_analysis_queries.md
│   ├── mysql_query_outputs/
│   └── superstore_erd_db_diagram.png
│
├── powerbi/
│   ├── superstore_dashboard.pbix
│   └── dashboard_screenshots/
│
└── README.md

---

## 1. Python — Data Cleaning 

Steps performed in the data cleaning script:

- Parsed order and ship dates using correct day-first formatting  
- Created derived features: delivery_days, weekday/weekend flag, month, quarter, year, day name  
- Standardized text columns (trimmed whitespace, fixed encoding issues, converted to lowercase)  
- Imputed missing postal codes  
- Renamed all columns into SQL-friendly snake_case  
- Exported the cleaned dataset into CSV and loaded it into MySQL for modeling
  
 [superstore_raw_dataset](python/SuperStore_dataset_cleaned.ipynb)
 
 [superstore_clean_python_script](superstore_raw_dataset/SuperStore_raw_dataset.csv)
 
 [superstore_cleaned_dataset](superstore_cleaned_dataset/Superstore_cleaned_final.csv)
 
## 2. Python - Predictive Sales Forecasting 

Steps performed in the predictive analysis script:

- Aggregated daily sales for time-series modeling  
- Modeled trend and weekly seasonality using Holt-Winters Exponential Smoothing  
- Generated a 7-day sales forecast with 95% confidence intervals  
- Visualized historical trends (30-day, 90-day) and forecast curves  
- Exported the forecast output for dashboarding  

 [superstore_predictive_analysis_python_script](python/SuperStore_Predictive_Analysis.ipynb)
 
 [superstore_predictive_analysis_7days_forecast](python/forecast_next_7_days.csv)
 
Screenshots: 

<img width="1023" height="394" alt="image" src="https://github.com/user-attachments/assets/3cecba31-1845-49a6-ac29-dcb012916773" />


<img width="1004" height="372" alt="image" src="https://github.com/user-attachments/assets/df381475-383f-4b6a-b7fb-fe7c9b1f4bf5" />


<img width="1189" height="490" alt="image" src="https://github.com/user-attachments/assets/bdce73d6-a01f-454b-a869-644860d38d11" />


## Key Outcomes (Python)

* Fully cleaned, structured dataset for SQL modeling

* Engineered analytical fields: date parts, delivery KPIs, weekday/weekend

* Consistent text formatting for dimension table joins

* Automated load into MySQL

* 7-day sales forecast using Holt-Winters exponential smoothing

---

## 3. MySQL — Data Modeling & ETL

Steps performed in the data modeling and ETL process:

- Designed a complete **Star Schema** optimized for analytical queries  
- Created **dimension tables** for products, customers, regions, orders, shipping details, and dates  
- Built a **central fact table** (superstore_sales) containing sales, delivery metrics, and foreign keys  
- Implemented surrogate keys (AUTO_INCREMENT) for all dimensions  
- Cleaned and standardized keys to avoid join inconsistencies  
- Created a unified **date dimension (date_info)** capturing full calendar attributes for both order and ship dates  
- Engineered a custom calendar generator using number tables to populate all dates between min/max ranges  
- Loaded cleaned Superstore data into MySQL from Python using SQLAlchemy  
- Applied ETL mappings to join raw data to the correct dimension keys  
- Validated row counts between source and fact table  
- Verified that sales totals matched between source (`superstore_cleaned`) and fact table (`superstore_sales`)  
- Ensured referential integrity between fact and dimension tables  

Database Components:

- product_info (Product Dimension)  
- customer_info (Customer Dimension)  
- region_info (Geographic Dimension)  
- order_info (Order Dimension)  
- shipping_info (Ship Mode Dimension)  
- date_info (Calendar / Date Dimension)  
- superstore_sales (Fact Table)

[superstore_data_modelling_sql_script](mysql/data_modelling&_ETL.md)
 
[superstore_star_schema](mysql/superstore_erd_db_diagram.png)

 Screenshot:

 <img width="1167" height="1232" alt="image" src="https://github.com/user-attachments/assets/41260717-9ce0-4c5c-a431-628ae392d551" />

---

## 4. MySQL — Analytical SQL Queries

Steps performed in SQL analysis:

- Executed queries to analyze sales, profitability, customer behavior, product performance, and shipping efficiency  
- Generated YoY sales trends  
- Identified top-performing categories, subcategories, and products  
- Ranked customers by total sales and order volume  
- Calculated segment-wise KPIs (sales, order counts, AOV)  
- Performed regional and state-level sales analysis  
- Evaluated shipping mode performance and average delivery time  
- Classified shipments into on-time vs late categories  
- Measured delivery trends over time (yearly averages)  
- Assessed customer shipping preferences by segment  
- Calculated quarterly revenue distribution  
- Evaluated average order value trends  
- Determined category contribution percentages to total revenue  
- Exported outputs as CSV files for dashboarding  

[superstore_mysql_analysis_queries](mysql/mysql_analysis_queries.md)

[superstore_mysql_analysis_outputs](mysql/mysql_query_outputs)

## Key Outcomes (SQL)

- Fully implemented **Star Schema** enabling efficient analytic queries  
- Accurate and validated fact table with perfect row & sales matching  
- Clean mapping between raw data → dimensions → fact  
- Rich date dimension powering trend, seasonality, and calendar analysis  
- 15+ SQL reports answering real business questions  
- Export-ready outputs feeding Power BI dashboards

---
  
## 5. Power BI — Dashboarding & Business Insights

Steps performed in the Power BI dashboard development:

- Connected Power BI to the cleaned MySQL dataset / exported CSV files  
- Built a fully interactive, multi-page dashboard for business stakeholders  
- Designed KPI cards for quick executive visibility (Sales, Orders, AOV, Profit Estimate)  
- Created trend visuals for yearly, quarterly, and monthly sales patterns  
- Visualized customer behavior across segments and geographies  
- Built product performance views for category, subcategory, and product-level analysis  
- Developed operational views to analyze shipping mode efficiency and delivery KPIs  
- Applied drill-downs, hierarchies, slicers, and cross-filtering for dynamic exploration  
- Ensured clean layout, consistent theme, and business-friendly storytelling  

### Dashboard Pages:

- **Executive Overview**  
  - Total Sales  
  - Estimated Profit (based on estimated average margin)  
  - Total Orders  
  - Average Order Value  
  - YoY Growth and Trend Lines  

- **Sales Performance**  
  - Monthly and quarterly trend analysis  
  - YoY comparison charts  
  - Sales by region and state  
  - Seasonal patterns  

- **Customer Insights**  
  - Segment-wise sales and order breakdown  
  - Top 10 customers  
  - Customer behavioral patterns (AOV, frequency)  

- **Product Performance**  
  - Category and subcategory contribution  
  - Top-selling products  
  - Product-level revenue distribution  

- **Shipping & Operations**  
  - Delivery days trend  
  - On-time vs Late shipments  
  - Ship mode efficiency  
  - Region-wise delivery performance  

[superstore_powerbi_dashboard](powerbi/Superstore_Dashboard.pbix)

⚠️ Note: Power BI `.pbix` files cannot be previewed on GitHub.  
Download and open in **Power BI Desktop** to view the interactive version.

Screenshots:

<img width="1216" height="676" alt="image" src="https://github.com/user-attachments/assets/530b2331-2b37-4682-b426-5dc3efd537a7" />


<img width="1204" height="679" alt="image" src="https://github.com/user-attachments/assets/1fb1f815-1b09-48f2-a4bd-4bf0a77c873f" />


<img width="1201" height="678" alt="image" src="https://github.com/user-attachments/assets/63592cf6-7ade-432b-8dbe-d9cd5f012010" />


<img width="1209" height="675" alt="image" src="https://github.com/user-attachments/assets/a0c77e8b-c6eb-47a2-a64c-3eb8a03bbf59" />


## Key Outcomes (Power BI)

- Complete business-ready dashboard with multi-page navigation  
- Executive-friendly KPI view of sales, orders, profitability, and trends  
- Deep insights into customer behavior and product performance  
- Real-world operational KPIs for shipping and delivery performance  
- Integrated 7-day sales forecast for data-driven planning  
- Clean, interactive, and visually consistent dashboards optimized for storytelling  
