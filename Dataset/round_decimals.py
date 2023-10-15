import pandas as pd

# Read the CSV file
data = pd.read_csv('aggregated_weather4.csv')

# Identify numeric columns
numeric_columns = data.select_dtypes(include=['number'])

# Round numeric columns to 2 decimal places
data[numeric_columns.columns] = data[numeric_columns.columns].round(2)

# Save the modified data to a new CSV file
data.to_csv('aggregate_weather.csv', index=False)
 