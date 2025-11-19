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

Python serves as the starting point of this project.  
Two scripts handle the full pipeline:

1. `cleaning_upload.py` — data cleaning, transformation, feature engineering  
2. `predictive_upload.py` — daily sales forecasting using Holt-Winters exponential smoothing  

Both outputs feed into the MySQL warehouse and Power BI dashboards.

---

### 1. Data Cleaning & Feature Engineering (cleaning_upload.py)

#### Loading the dataset

#### Parsing date columns (DD-MM-YYYY format)

#### Delivery lead time calculation

#### Imputing missing postal codes

#### Cleaning all text fields

#### Weekday vs Weekend classification

#### Export cleaned dataset

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

