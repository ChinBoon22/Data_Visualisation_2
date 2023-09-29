import pandas as pd

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('Global_Weather_Repository_Cleaned.csv')

# Define the columns you want to aggregate
columns_to_aggregate = ['gust_mph', 'visibility_km',
                        'uv_index', 'air_quality_Ozone']

# Group by 'country' and 'continent', and calculate the mean for each specified column
aggregated_df = df.groupby(['continent'])[
    columns_to_aggregate].mean().reset_index()

aggregated_df[['gust_mph', 'visibility_km',
               'uv_index', 'air_quality_Ozone']] = aggregated_df[[
                   'gust_mph', 'visibility_km',
                   'uv_index', 'air_quality_Ozone']].round(2)

# Now, filtered_df contains only rows where "wind_direction" is one of the specified values
# Save the aggregated data to a new CSV file
aggregated_df.to_csv('aggregated_data_no_pivot.csv', index=False)
