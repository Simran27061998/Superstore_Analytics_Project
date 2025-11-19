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

## Python — Data Cleaning & Predictive Sales Forecasting

## Data Cleaning (Python)

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
 
### 2. Predictive Sales Forecasting (predictive_upload.py)

#### Aggregate daily sales

#### Holt-Winters Exponential Smoothing (Trend + Weekly Seasonality)

#### Confidence intervals (95%)

#### Trend visualizations generated

* Last 90 days

* Last 30 days

* Forecast vs actuals

#### Export forecast results


### Key Outcomes (Python)

* Fully cleaned, structured dataset for SQL modeling

* Engineered analytical fields: date parts, delivery KPIs, weekday/weekend

* Consistent text formatting for dimension table joins

* Automated load into MySQL

* 7-day sales forecast using Holt-Winters exponential smoothing

