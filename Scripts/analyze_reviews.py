import nltk
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Ensure nltk data directory is correct
nltk.data.path.append('/Users/hasaannoor/nltk_data')

# Import the stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Load dataMovie Review Trend Analysis
reviews_path = 'data/Scraped_Movie_Reviews.csv'
numbered_info_path = 'data/Filtered_Movie_Info.csv'

reviews_df = pd.read_csv(reviews_path)
filtered_info_df = pd.read_csv(numbered_info_path)

# Extract year
filtered_info_df['year'] = filtered_info_df['release_date'].str.extract(r'(\d{4})')
filtered_info_df = filtered_info_df.dropna(subset=['year'])
filtered_info_df['year'] = filtered_info_df['year'].astype(int)
filtered_info_df = filtered_info_df[(filtered_info_df['year'] >= 1970) & (filtered_info_df['year'] <= 2024)]

# Merge dataframes
merged_df = pd.merge(reviews_df, filtered_info_df, on='title')

# Function to get polarity
def get_polarity(text):
    if pd.isna(text):
        return None
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to get subjectivity
def get_subjectivity(text):
    if pd.isna(text):
        return None
    blob = TextBlob(text)
    return blob.sentiment.subjectivity

# Function to get sentiment category
def get_sentiment_category(polarity):
    if pd.isna(polarity):
        return None
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply polarity and subjectivity analysis
for column in ['review_1', 'review_2', 'review_3', 'review_4', 'review_5']:
    merged_df[column + '_polarity'] = merged_df[column].apply(get_polarity)
    merged_df[column + '_subjectivity'] = merged_df[column].apply(get_subjectivity)

# Calculate average polarity and subjectivity
merged_df['average_polarity'] = merged_df[['review_1_polarity', 'review_2_polarity', 'review_3_polarity', 'review_4_polarity', 'review_5_polarity']].mean(axis=1)
merged_df['average_subjectivity'] = merged_df[['review_1_subjectivity', 'review_2_subjectivity', 'review_3_subjectivity', 'review_4_subjectivity', 'review_5_subjectivity']].mean(axis=1)

# Apply sentiment category analysis
merged_df['average_sentiment'] = merged_df['average_polarity'].apply(get_sentiment_category)

# Group by year and calculate the average polarity, subjectivity, and sentiment distribution for each year
polarity_trend_df = merged_df.groupby('year')['average_polarity'].mean().reset_index()
subjectivity_trend_df = merged_df.groupby('year')['average_subjectivity'].mean().reset_index()
sentiment_distribution_df = merged_df.groupby(['year', 'average_sentiment']).size().unstack(fill_value=0)

# Plot polarity trend over time
plt.figure(figsize=(12, 6))
plt.plot(polarity_trend_df['year'], polarity_trend_df['average_polarity'], marker='o', label='Average Polarity')
plt.axhline(y=0, color='r', linestyle='--', label='Neutral Polarity')
plt.title('Average Movie Review Polarity Over Time (1970-2024)')
plt.xlabel('Year')
plt.ylabel('Average Polarity')
plt.grid(True)

# Create invisible lines for custom legend entries
invisible_line = plt.Line2D([0], [0], color='w', linestyle='None')
plt.legend([plt.Line2D([0], [0], color='b'), plt.Line2D([0], [0], color='r', linestyle='--')],
           ['Average Polarity', 'Neutral Polarity'],
           loc='upper left', title='Polarity Key')

plt.show()

# Plot subjectivity trend over time
plt.figure(figsize=(12, 6))
plt.plot(subjectivity_trend_df['year'], subjectivity_trend_df['average_subjectivity'], marker='o', label='Average Subjectivity')
plt.title('Average Movie Review Subjectivity Over Time (1970-2024)')
plt.xlabel('Year')
plt.ylabel('Average Subjectivity')
plt.grid(True)

# Add custom legend
handles, labels = plt.gca().get_legend_handles_labels()
handles.append(plt.Line2D([0], [0], color='blue', label='0.0 = Objective'))
handles.append(plt.Line2D([0], [0], color='blue', label='1.0 = Subjective'))
plt.legend(handles=handles, loc='upper left')

plt.show()

# Plot sentiment distribution over time
sentiment_distribution_df = sentiment_distribution_df.div(sentiment_distribution_df.sum(axis=1), axis=0)

plt.figure(figsize=(12, 6))
plt.stackplot(sentiment_distribution_df.index, 
              sentiment_distribution_df['Positive'], 
              sentiment_distribution_df['Neutral'], 
              sentiment_distribution_df['Negative'],
              labels=['Positive', 'Neutral', 'Negative'],
              colors=['green', 'yellow', 'red'])
plt.title('Movie Review Sentiment Distribution Over Time (1970-2024)')
plt.xlabel('Year')
plt.ylabel('Proportion')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()