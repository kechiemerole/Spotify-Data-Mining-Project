# Spotify Exploratory Data Analysis
![image](https://github.com/kechiemerole/Spotify-Data-Mining-Project/assets/97633203/6fc7e9e6-6f88-4033-9ebf-66024413d3bf)

## Project Pipeline
1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Clustering and Segmentation
5. Predictive Modeling
6. Evaluation and Validation
7. Conclusion and Results

### Questions
1. Does the season of the year determine listening habits?
2. Is there a correlation between the duration of listening sessions and specific artists?
3. Are there any notable trends or patterns in the listening history over time?
4. What are the most listened to artists, or songs in my data?

## Introduction
Spotify is a widely recognized digital music streaming service that originated in April 2006 in Stockholm, Sweden. Over the years, it has established itself as a dominant force in the music industry, offering a vast collection of songs, podcasts, and other audio content to its users.

As a devoted user of Spotify, I have personally experienced the transformative impact it has had on the way we consume music. Through its innovative platform, Spotify has effectively popularized the concept of music streaming, providing users like myself with a convenient and easily accessible medium to explore, enjoy, and share favorite tracks.

## Project Overview 
As an avid user of Spotify, I have embarked on a project to analyze and gain insights into my listening habits using data mining techniques and exploratory data analysis. The primary objective is to visualize patterns and trends in the music I engage with, ultimately aiming to replicate Spotify's yearly wrapped summary of my most listened-to artists, songs, and genres. This will be achieved by employing machine learning algorithms and prediction techniques to forecast the results based on the current data. By employing Jupyter notebooks and popular Python libraries such as NumPy, Panda, and Sci-kit learn, I aim to extract meaningful patterns and trends from the data. Furthermore, I will leverage machine learning algorithms such as KNN and regression techniques to predict and replicate Spotify's yearly wrapped summary of the most listened-to artists, songs, and genres based on the available dataset.

## Project Plan 
### Data Collection
To commence this project, I have acquired a copy of the basic package of my Spotify data, which encompasses a comprehensive set of information related to my streaming and listening activities. The data package includes details such as playlists, streaming history from the past year, items saved in my library, search queries, follower counts, accounts followed, blocked accounts, payment and subscription data, user information, customer service history, family plan data, inferences, voice inputs, podcast interactivity, and Spotify for Artists data.

The data has been obtained from my Spotify listening history at https://www.spotify.com/ca-en/account/privacy/ using the “Download your data tool”. The preparation time for this request took about 5 business days. The data spans from July 2, 2022 to July 2, 2023 which is a years worth of my listening habits.

### Data Preprocessing 
At this stage, I have successfully extracted the data from the downloaded Spotify package, encompassing user listening history, playlists, artists, and albums. However, since the raw data is initially in JSON format, it necessitates conversion to a more manageable format for analysis, such as CSV.

To streamline this process I converted all the streaming history files, namely StreamingHistory0, StreamingHistory1, and StreamingHistory2, into the CSV format. This ensures uniformity and facilitates seamless data integration.

Subsequently, utilizing the robust capabilities of the Pandas library, I employ methods such as append, merge, and concat to consolidate the CSV files. This enables the aggregation of comprehensive data sets without compromising data integrity or introducing errors associated with manual data manipulation.

Moreover, to ensure data accuracy and reliability, I have diligently cleaned the datasets. This entails addressing missing values and identifying and appropriately handling outliers. 

The resulting dataset from preprocessing contains <b>28,995</b> rows and <b>4</b> columns.

### Data Analysis
Using data mining techniques and exploratory data analysis, I will delve into the acquired Spotify data to uncover valuable insights about my music consumption patterns. By examining factors such as play counts, duration, genre preferences, and temporal trends, I aim to gain a deeper understanding of my musical preferences and habits.

### Data Visualization
Through the utilization of data visualization methods, I will present the findings of the data analysis in a clear and visually appealing manner. This will include interactive visualizations, charts, and graphs to illustrate trends, relationships, and notable patterns in my listening habits.

### Machine Learning and Prediction
The project will progress to the application of machine learning algorithms and prediction techniques to replicate Spotify's yearly wrapped summary. By leveraging the historical data and utilizing prediction algorithms, I will strive to forecast the most listened-to artists, songs, and genres based on the current dataset. This predictive approach will provide valuable insights into potential future preferences and trends.
