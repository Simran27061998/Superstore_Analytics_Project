# %%
#import cleaned Superstore dataset

import pandas as pd

df = pd.read_csv("Superstore_cleaned_final.csv", parse_dates=["order_date", "ship_date"])

print(df.info())

# %%
#Check Shape of dataset

print(df.shape)

# %%
#Check if any values failed to parse

failed_order = df['order_date'].isna().sum()
failed_ship = df['ship_date'].isna().sum()
print(failed_order)
print(failed_ship)

# %%
#Predicting next 7 days sales

daily_sales = (df.groupby('order_date',as_index=False)['sales'].sum().rename(columns={'order_date':'ds','sales':'y'}))

#groupby - groups dataset by order_date(one row for each day of sales)
#['sales'] - selecting only sales column as we want just sum of the sales on a day
#Prophet has strict naming requirements. The date columns must me named 'ds' and value column must be named 'y'


# %%
#Check the daily_sales column

print(daily_sales)

# %%
#Visualize daily sales over time

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.figure(figsize=(12,4))
plt.plot(daily_sales['ds'], daily_sales['y'], marker='.', linewidth=0.6, color='blue')
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(alpha=0.3)


# Format x-axis to show full dates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()  # Rotate for readability
plt.show()

# %%
#Train Prophet model and forecast next 7 days

from prophet import Prophet #Creates the forecasting model with built-in seasonality.


#Initialize model

m = Prophet(daily_seasonality=False, # we don’t need hourly/daily patterns
            weekly_seasonality=True, # weekly effects are useful for retail
            yearly_seasonality=True,  # capture long-term trends
            changepoint_prior_scale=0.05,  # smooth trend
    seasonality_mode='additive'   # more stable than 'multiplicative'
)

#Fit model to daily sales data

m.fit(daily_sales) #Learns from your 2015–2018 data.

#Create a future dataframe for the next 7 days

future = m.make_future_dataframe(periods=7,freq='D') #create 7 more future dates spaced one day apart

#Predict Sales for future dates

forecast = m.predict(future)

#Display the last 7 days predictions

# Display the last 7 predictions
pred_next_7 = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7).reset_index(drop=True)
print("Next 7 Days Forecast:")
print(pred_next_7.to_string(index=False))

# %%
# Holt-Winters fallback to predict next 7 days forecast
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pandas as pd
import matplotlib.pyplot as plt

ts = daily_sales.set_index('ds')['y'].asfreq('D')    # your daily series
ts = ts.fillna(0)   # fill gaps (or use .ffill() if you prefer)

hw = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=7, initialization_method="estimated")
hw_fit = hw.fit(optimized=True)

# Forecast 7 days
pred_hw = hw_fit.forecast(7)

# Convert to DataFrame for readability
pred_df = pred_hw.reset_index()
pred_df.columns = ['ds', 'yhat']

print("Holt-Winters 7-day forecast:")
print(pred_df.to_string(index=False))

# Plot last 90 days + forecast
future_idx = pd.date_range(start=ts.index[-1] + pd.Timedelta(days=1), periods=7, freq='D')
plt.figure(figsize=(12,4))
plt.plot(ts[-90:], label='history')
plt.plot(future_idx, pred_hw.values, marker='o', label='forecast (HW)', color='orange')
plt.legend(); plt.title('Holt-Winters: Last 90 days + 7-day forecast'); plt.show()


# %%
# Plot last 30 days of history + 7-day HW forecast with approximate 95% CI
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assumes these already exist in your session:
# ts            -> pd.Series indexed by ds (daily), the historical series used for HW
# hw_fit        -> fitted ExponentialSmoothingResults object
# pred_df       -> DataFrame with columns ['ds','yhat'] for the 7 forecast days

# 1) Prepare history and forecast frames
history_days = 30
hist = ts[-history_days:].reset_index().rename(columns={ts.name: 'y'})  # last 30 days
forecast = pred_df.copy()
forecast['ds'] = pd.to_datetime(forecast['ds'])

# 2) Approximate 95% CI for forecast using residual std
#    residuals = actual - fitted_values (aligned)
fitted = hw_fit.fittedvalues  # aligned with ts index
resid = (ts - fitted).dropna()
resid_std = resid.std()

z = 1.96  # 95% approx
forecast['yhat_lower'] = forecast['yhat'] - z * resid_std
forecast['yhat_upper'] = forecast['yhat'] + z * resid_std

# 3) Plot
plt.figure(figsize=(12,5))

# plot historical last 30 days
plt.plot(hist['ds'], hist['y'], label=f'History (last {history_days} days)', marker='o')

# plot forecast points
plt.plot(forecast['ds'], forecast['yhat'], label='Forecast (HW)', marker='o', color='orange')

# plot CI as shaded area
plt.fill_between(forecast['ds'].astype('datetime64[ns]'),
                 forecast['yhat_lower'],
                 forecast['yhat_upper'],
                 color='orange', alpha=0.2, label='Approx. 95% CI')

# formatting
plt.title(f'Last {history_days} days + 7-day Holt-Winters Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=30)
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()

# 4) Save forecast to CSV
forecast_out = forecast[['ds','yhat','yhat_lower','yhat_upper']].copy()
forecast_out.to_csv('forecast_next_7_days.csv', index=False)
print("Saved forecast_next_7_days.csv")



