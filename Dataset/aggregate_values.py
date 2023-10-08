import pandas as pd

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('Global_Weather_Repository_Cleaned.csv')

# Define the columns you want to aggregate
columns_to_aggregate = ['gust_mph', 'visibility_km',
                        'uv_index', 'air_quality_Ozone']

# Group by 'country' and 'continent', and calculate the mean for each specified column
aggregated_df = df.groupby(['continent', 'country'])[
    columns_to_aggregate].mean().reset_index()

aggregated_df[['gust_mph', 'visibility_km',
               'uv_index', 'air_quality_Ozone']] = aggregated_df[[
                   'gust_mph', 'visibility_km',
                   'uv_index', 'air_quality_Ozone']].round(2)

# Assuming you have the final aggregated dataset in a DataFrame called 'final_aggregated_df'
# Sort the DataFrame by 'air_quality_Ozone' column in descending order
final_aggregated_df = aggregated_df.sort_values(
    by='air_quality_Ozone', ascending=False)

# Select the top 20 rows
top_20_countries_df = final_aggregated_df.head(20)
countries_list = top_20_countries_df['country'].unique().tolist()


# Group by 'country' and 'continent', and calculate the mean for each specified column
df = df[df['country'].isin(countries_list)]
aggregated_df_time = df.groupby(['continent', 'country', 'last_updated_day'])[
    columns_to_aggregate].mean().reset_index()

aggregated_df_time[['gust_mph', 'visibility_km',
                    'uv_index', 'air_quality_Ozone']] = aggregated_df_time[[
                        'gust_mph', 'visibility_km',
                        'uv_index', 'air_quality_Ozone']].round(2)

# Now, filtered_df contains only rows where "wind_direction" is one of the specified values
# Save the aggregated data to a new CSV file
aggregated_df_time.to_csv('2_wind_data.csv', index=False)
