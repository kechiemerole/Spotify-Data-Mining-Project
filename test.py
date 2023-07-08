import pandas as pd
import matplotlib.pyplot as plt

# Read the Spotify dataset into a DataFrame
data = pd.read_csv("myDataCombined.csv")



# Convert the date column to datetime datatype
data['endTime'] = pd.to_datetime(data['endTime'])

# Filter the data for the desired date range
start_date = pd.to_datetime('2022-07-02')
end_date = pd.to_datetime('2023-07-02')
filtered_data = data[(data['endTime'] >= start_date) & (data['endTime'] <= end_date)]

# Group the filtered data by month and sum the minutes played
monthly_minutes = filtered_data.groupby(filtered_data['endTime'].dt.to_period('M'))['msPlayed'].sum()

# Plot the histogram of minutes played by month
plt.bar(monthly_minutes.index, monthly_minutes.values)
plt.xlabel('Month')
plt.ylabel('Total Minutes Played')
plt.title('Minutes Played by Month (July 2022 - July 2023)')
plt.xticks(rotation=45)
plt.show()
