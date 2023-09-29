import pandas as pd

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('Global_Weather_Repository_Cleaned.csv')

# Define the columns you want to aggregate
columns_to_aggregate = ['gust_mph', 'pressure_mb', 'wind_kph', 'pressure_in', 'visibility_km',
                        'uv_index', 'air_quality_Ozone', 'air_quality_Nitrogen_dioxide', 'air_quality_Sulphur_dioxide', 'air_quality_PM2.5', 'air_quality_PM10', 'air_quality_us-epa-index', 'air_quality_gb-defra-index']

# Group by 'country' and 'continent', and calculate the mean for each specified column
aggregated_df = df.groupby(['continent'])[
    columns_to_aggregate].mean().reset_index()

aggregated_df[['gust_mph', 'pressure_mb', 'wind_kph', 'pressure_in', 'visibility_km',
               'uv_index', 'air_quality_Ozone', 'air_quality_Nitrogen_dioxide', 'air_quality_Sulphur_dioxide', 'air_quality_PM2.5', 'air_quality_PM10', 'air_quality_us-epa-index', 'air_quality_gb-defra-index']] = aggregated_df[[
                   'gust_mph', 'pressure_mb', 'wind_kph', 'pressure_in', 'visibility_km',
                   'uv_index', 'air_quality_Ozone', 'air_quality_Nitrogen_dioxide', 'air_quality_Sulphur_dioxide', 'air_quality_PM2.5', 'air_quality_PM10', 'air_quality_us-epa-index', 'air_quality_gb-defra-index']].round(2)

# Now, filtered_df contains only rows where "wind_direction" is one of the specified values
# Save the aggregated data to a new CSV file
aggregated_df.to_csv('aggregated_data_for_stream_graph.csv', index=False)
