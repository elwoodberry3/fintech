# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from prophet import Prophet  # For forecasting

# Load the trading dataset
# Assuming the file 'trading_data.csv' has columns: Date, Asset, Type, Quantity, Price, Fees, P/L
data = pd.read_csv("trading_data.csv")

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Clean data
# Drop rows with missing values
data.dropna(inplace=True)

# Add a column for net profit/loss after fees
data['Net_PnL'] = data['P/L'] - data['Fees']

# Add a column for cumulative profit/loss
data['Cumulative_PnL'] = data['Net_PnL'].cumsum()

# Calculate asset-level performance
asset_performance = data.groupby('Asset').agg(
    Total_PnL=('Net_PnL', 'sum'),
    Average_Return=('Net_PnL', 'mean'),
    Volatility=('Net_PnL', 'std')
).reset_index()

# Export asset performance to a CSV for Tableau
asset_performance.to_csv("asset_performance.csv", index=False)

# Calculate daily performance
daily_performance = data.groupby('Date').agg(
    Total_PnL=('Net_PnL', 'sum'),
    Volatility=('Net_PnL', 'std')
).reset_index()

# Add a rolling average for smoother trends
daily_performance['Rolling_Avg_PnL'] = daily_performance['Total_PnL'].rolling(window=7).mean()

# Export daily performance to a CSV for Tableau
daily_performance.to_csv("daily_performance.csv", index=False)

# Time-Series Forecasting using Prophet
# Prepare data for Prophet
forecast_data = daily_performance[['Date', 'Total_PnL']].rename(columns={'Date': 'ds', 'Total_PnL': 'y'})

# Initialize Prophet model
model = Prophet()
model.fit(forecast_data)

# Create a dataframe for future dates
future = model.make_future_dataframe(periods=30)  # Forecast for the next 30 days

# Predict future performance
forecast = model.predict(future)

# Export forecasted data to a CSV for Tableau
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("forecasted_performance.csv", index=False)

# Visualize the forecast
fig = model.plot(forecast)
plt.title("Forecasted Trading Performance")
plt.show()

# Correlation Analysis (optional)
# Analyze correlations between asset types
correlation_data = data.pivot_table(index='Date', columns='Asset', values='Net_PnL', aggfunc='sum')
correlation_matrix = correlation_data.corr()

# Export correlation matrix to a CSV for Tableau
correlation_matrix.to_csv("correlation_matrix.csv")

# Save cleaned and processed data for Tableau
data.to_csv("processed_trading_data.csv", index=False)

# Print a summary of the analysis
print("Data preprocessing and analysis complete!")
print(f"Total unique assets: {data['Asset'].nunique()}")
print(f"Processed dataset saved as 'processed_trading_data.csv'")
