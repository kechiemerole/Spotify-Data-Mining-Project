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

# Count the occurrences of each artist
artist_counts = data['artistName'].value_counts()

# Select the top 10 artists
top_10_artists = artist_counts.head(10)

# Plot the bar chart for the top 10 artists
plt.bar(top_10_artists.index, top_10_artists.values)
plt.xlabel('Artist')
plt.ylabel('Number of Listens')
plt.title('Top 10 Most Listened to Artists')
plt.xticks(rotation=90)
plt.show()

track_counts = data['trackName'].value_counts()

# Select the top 10 artists
top_10_tracks = track_counts.head(10)

# Plot the bar chart for the top 10 artists
plt.bar(top_10_tracks.index, top_10_tracks.values)
plt.xlabel('Track')
plt.ylabel('Number of Listens')
plt.title('Top 10 Most Listened to Tracks')
plt.xticks(rotation=90)
plt.show()

