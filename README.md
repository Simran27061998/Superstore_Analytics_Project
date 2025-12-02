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

```
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

```
---

## 1. Python — Data Cleaning 

Steps performed in the data cleaning script:

- Parsed order and ship dates using correct day-first formatting  
- Created derived features: delivery_days, weekday/weekend flag, month, quarter, year, day name  
- Standardized text columns (trimmed whitespace, fixed encoding issues, converted to lowercase)  
- Imputed missing postal codes  
- Renamed all columns into SQL-friendly snake_case  
- Exported the cleaned dataset into CSV and loaded it into MySQL for modeling
  
 [superstore_raw_dataset](superstore_raw_dataset/SuperStore_raw_dataset.csv)
 
 [superstore_clean_python_script](python/SuperStore_dataset_cleaned.ipynb)
 
 [superstore_cleaned_dataset](superstore_cleaned_dataset/Superstore_cleaned_final.csv)

---

## 2. MySQL — Data Modeling & ETL

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

## 3. MySQL — Analytical SQL Queries

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
  
## 4. Power BI — Dashboarding & Business Insights

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

[superstore_powerbi_dashboard](power_bi/Superstore_Dashboard.pbix)

[superstore_powerbi_dax_measures](power_bi/dax_measures.md)

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

---

## Conclusion & Key Takeaways

This project demonstrates a complete end-to-end Business Intelligence workflow using real retail data.  
From raw data to executive dashboards, every stage of the analytics pipeline was designed, executed, and validated with production-grade best practices.

### What This Project Showcases

- **Strong data cleaning & preprocessing skills** using Python  
- **Advanced SQL capabilities** including dimensional modeling, ETL, and analytical queries  
- **Professional BI reporting** through interactive Power BI dashboards  
- Ability to perform **trend analysis, customer segmentation, product insights, and operational KPIs**  
- Use of **forecasting (Holt-Winters)** to provide forward-looking insights  
- End-to-end understanding of how data flows through a modern analytics ecosystem  

### Business Impact

The project provides stakeholders with:

- Clarity on **sales trends and seasonality**  
- Visibility into **customer value segments**  
- Understanding of **product performance** and revenue drivers  
- Insight into **shipping efficiency** and operational bottlenecks  
- A **prediction model** to support short-term sales planning  

### Technical Impact

- Fully functional **Star Schema** supporting analytical workloads  
- Cleaned, validated, and SQL-optimized dataset  
- Reusable data pipeline connecting Python → MySQL → Power BI  
- Exported SQL outputs enabling easy reporting and dashboard integration  

---

## How to Reproduce This Project

To run this project end-to-end, follow the steps below. The process mirrors a real analytics workflow from Python → MySQL → Power BI.

### Python Setup

- Install the required Python dependencies (Pandas, NumPy, Statsmodels, SQLAlchemy, PyMySQL).
- Run the data cleaning script to parse dates, engineer features, clean text, and generate the final CSV.
- Execute the forecasting script to model weekly seasonality, generate a 7-day forecast, and export predictions.
- Ensure both outputs — cleaned dataset and forecast — are stored in the /python folder.

### MySQL Setup

- Create a new MySQL database (superstore_db).
- Run all scripts inside the /mysql directory:
- Dimension tables (product, customer, region, order, shipping, date).
- Fact table (superstore_sales).
- ETL joins connecting cleaned data to dimensional keys.
- Validate the pipeline with row count checks and sales reconciliation.
- Run the analytical SQL queries to generate CSV outputs for Power BI.

### Power BI Setup

- Open superstore_dashboard.pbix in Power BI Desktop.
- Connect to the MySQL database or point to the exported CSVs.
- Refresh the model so updated SQL and Python outputs sync with visuals.
- Explore dashboard pages covering executive KPIs, sales trends, customer insights, product performance, and operational metrics.

---

## For questions, feedback, or collaboration opportunities, feel free to connect via GitHub or LinkedIn.

---
