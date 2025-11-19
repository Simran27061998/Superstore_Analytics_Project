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
 
### 2. Python - Predictive Sales Forecasting 

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


### Key Outcomes 

* Fully cleaned, structured dataset for SQL modeling

* Engineered analytical fields: date parts, delivery KPIs, weekday/weekend

* Consistent text formatting for dimension table joins

* Automated load into MySQL

* 7-day sales forecast using Holt-Winters exponential smoothing

