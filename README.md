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
```python

df = pd.read_csv('SuperStore_raw_dataset.csv')

```
#### Parsing date columns (DD-MM-YYYY format)

```python

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=True)
df['Ship Date']  = pd.to_datetime(df['Ship Date'],  errors='coerce', dayfirst=True)

```
#### Delivery lead time calculation

```python

df['delivery_days'] = (df['Ship Date'] - df['Order Date']).dt.days

```
#### Imputing missing postal codes

```python

df['Postal Code'] = df['Postal Code'].fillna(df['Postal Code'].mode()[0])

```
#### Cleaning all text fields

```python

for col in df.select_dtypes(include='object').columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.replace('\xa0', ' ', regex=False)
        .str.lower()
    )

```

#### SQL-friendly column names

```python

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
    .str.replace('/', '_')
)

```

#### Weekday vs Weekend classification

```python

df['type_of_day'] = df['order_day'].apply(
    lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday'
)

```
#### Export cleaned dataset

```python

df.to_csv('Superstore_cleaned_final.csv', index=False)

```

### 2. Predictive Sales Forecasting (predictive_upload.py)

#### Aggregate daily sales

```python

daily_sales = (
    df.groupby('order_date', as_index=False)['sales'].sum()
      .rename(columns={'order_date': 'ds', 'sales': 'y'})
)

```

#### Holt-Winters Exponential Smoothing (Trend + Weekly Seasonality)

```python

hw = ExponentialSmoothing(
        ts,
        trend='add',
        seasonal='add',
        seasonal_periods=7,
        initialization_method="estimated"
)
hw_fit = hw.fit(optimized=True)
pred_hw = hw_fit.forecast(7)

```

#### Confidence intervals (95%)

```python

resid_std = (ts - hw_fit.fittedvalues).dropna().std()
forecast['yhat_lower'] = forecast['yhat'] - 1.96 * resid_std
forecast['yhat_upper'] = forecast['yhat'] + 1.96 * resid_std

```

#### Trend visualizations generated

* Last 90 days

* Last 30 days

* Forecast vs actuals

#### Export forecast results

```python

forecast_out.to_csv('forecast_next_7_days.csv', index=False)

```

### Key Outcomes (Python)

* Fully cleaned, structured dataset for SQL modeling

* Engineered analytical fields: date parts, delivery KPIs, weekday/weekend

* Consistent text formatting for dimension table joins

* Automated load into MySQL

* 7-day sales forecast using Holt-Winters exponential smoothing

