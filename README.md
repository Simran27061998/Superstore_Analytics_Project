🛒 Superstore Analytics Project

End-to-end retail analytics using Python, MySQL, and Power BI

This project performs a complete analysis of the Superstore dataset (2015–2018) and demonstrates an industry-style analytics workflow:

Python → data cleaning, feature engineering, forecasting

MySQL → database modeling, ETL, SQL analysis

Power BI → dashboarding, KPI visualization

The goal is to simulate a real-world BI/Analytics workflow and present insights in both:

Technical Format → SQL, dimensional model, ETL

Business Format → interactive dashboards, KPIs, forecasting

🛠 Tools & Technologies

| Layer                       | Tools Used                                                   |
| --------------------------- | ------------------------------------------------------------ |
| Data Cleaning & Forecasting | Python (Pandas, NumPy, Statsmodels, SQLAlchemy, Matplotlib)  |
| Database & Modeling         | MySQL (Star Schema, Fact/Dim model, SQL queries)             |
| BI & Visualization          | Power BI (Executive, Product, Shipping, Customer dashboards) |
| Version Control             | Git, GitHub                                                  |


📁 Repository Structure

Superstore_Analytics_Project/
│
├── python/
│   ├── cleaning_upload.py                 # Data cleaning & feature engineering
│   ├── predictive_upload.py               # Sales forecasting
│   └── forecast_next_7_days.csv           # Model output
│
├── mysql/
│   ├── data_modelling&_ETL.md             # Star schema + ETL scripts
│   ├── mysql_analysis_queries.md          # Business SQL queries
│   ├── mysql_query_outputs/               # CSV outputs of SQL queries
│   └── superstore_erd_db_diagram.png      # ERD diagram
│
├── powerbi/
│   ├── superstore_dashboard.pbix          # Final dashboard
│   └── dashboard_screenshots/             # PNG screenshots
│
└── README.md


📘 Python: Data Cleaning & Predictive Sales Forecasting

(from cleaning_upload.py & predictive_upload.py)

This project begins with a Python workflow for preparing the Superstore dataset and generating a 7-day sales forecast. The cleaned output is loaded into MySQL for modelling and further analysis.
