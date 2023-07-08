# importing packages 
import json
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("myDataCombined.csv")
print(data)
# Check for null values
null_values = data.isnull().sum()

# Print the number of null values for each column
print(null_values)

# _________________________________________________________________________________________________
# Read the CSV file into a DataFrame
data = pd.read_csv("myDataCombined.csv")
data.describe()
data.info()


# Convert the duration of msPlayed to seconds from milliseconds 
data['duration_sec'] = data['msPlayed'].apply(lambda x: x / 1000)
data.drop('msPlayed', inplace = True, axis = 1)
print(data)


# Count the occurrences of each artist
artist_counts = data['artistName'].value_counts()

# Select the top 10 artists
top_10_artists = artist_counts.head(10)
spotify_green = ['#1DB954']
# Plot the bar chart for the top 10 artists
plt.bar(top_10_artists.index, top_10_artists.values, color=spotify_green)
plt.xlabel('Artist')
plt.ylabel('Number of Listens')
plt.title('Top 10 Most Listened to Artists')
plt.xticks(rotation=90)
plt.show()

track_counts = data['trackName'].value_counts()

# Select the top 10 artists
top_10_tracks = track_counts.head(10)

# Plot the bar chart for the top 10 artists
plt.bar(top_10_tracks.index, top_10_tracks.values, color=spotify_green)
plt.xlabel('Track')
plt.ylabel('Number of Listens')
plt.title('Top 10 Most Listened to Tracks')
plt.xticks(rotation=90)
plt.show()



# Read the Spotify dataset into a DataFrame
data = pd.read_csv("myDataCombined.csv")

# Convert the endtime column to a datetime datatype
data['endTime'] = pd.to_datetime(data['endTime'])

# Group the data by month and sum the duration played in milliseconds
monthly_duration = data.groupby(data['endTime'].dt.month)['msPlayed'].sum()

# Plot the duration played by month
plt.plot(monthly_duration.index, monthly_duration.values)
plt.xlabel('Month')
plt.ylabel('Duration (ms)')
plt.title('Duration Played by Month')
plt.xticks(range(1, 13))
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Read the Spotify dataset into a DataFrame
data = pd.read_csv("myDataCombined.csv")

# Convert the date column to datetime datatype
data['endTime'] = pd.to_datetime(data['endTime'])

# Classify dates into seasons
data['season'] = data['endTime'].dt.month.map({1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
                                            6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn',
                                            11: 'Autumn', 12: 'Winter'})

# Calculate minutes played by converting duration from milliseconds to minutes
# data['minutes_played'] = data['duration'] / 60000

# Group the data by season and sum the minutes played
seasonal_minutes = data.groupby('season')['msPlayed'].sum()

# Plot the histogram of minutes played by season
plt.bar(seasonal_minutes.index, seasonal_minutes.values, color=spotify_green)
plt.xlabel('Season')
plt.ylabel('Total Minutes Played')
plt.title('Minutes Played by Season')
plt.show()
