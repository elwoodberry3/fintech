# Preprocessing  

1. Data Cleaning
  1. Ensures the dataset is free of missing or erroneous values.
  1. Creates derived columns like Net_PnL and Cumulative_PnL for better analysis.

2. Performance Metrics
  2. Summarizes metrics for each asset and by day.
  2. Includes total P/L, average returns, and volatility.

3. Time-Series Forecasting
  3. Uses Prophet to predict future trading performance.
  3. Exports forecast results with confidence intervals for Tableau visualization.

4. Correlation Analysis
  4. Creates a pivot table to analyze relationships between assets.
  4. Provides a correlation matrix for advanced Tableau visualizations.

5. Output Files for Tableau  
  5. Cleaned trading data (processed_trading_data.csv).
  5. Asset-level performance (asset_performance.csv).
  5. Daily performance trends (daily_performance.csv).
  5. Forecasted trends (forecasted_performance.csv).
  5. Correlation matrix (correlation_matrix.csv).