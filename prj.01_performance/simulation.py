# CORTA BEAR CAPITAL - Dataset Simulation.

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dates
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Simulate trading data
np.random.seed(42)
data = {
    "Date": np.random.choice(date_range, 500),
    "Asset": np.random.choice(["US Bonds", "Forex", "Options"], 500),
    "Type": np.random.choice(["Call", "Put", "Spot"], 500),
    "Quantity": np.random.randint(1, 1000, 500),
    "Price": np.random.uniform(100, 5000, 500),
    "Fees": np.random.uniform(5, 50, 500),
    "P/L": np.random.uniform(-1000, 2000, 500),
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Net P/L and Cumulative P/L
df['Net_PnL'] = df['P/L'] - df['Fees']
df['Cumulative_PnL'] = df['Net_PnL'].cumsum()

# Save to CSV
df.to_csv("simulated_trading_data.csv", index=False)
print("Simulated dataset saved as 'simulated_trading_data.csv'")
