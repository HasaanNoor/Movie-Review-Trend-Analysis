import pandas as pd
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Load the movie info data
file_path = 'data/Movie_Info.csv'
movie_info = pd.read_csv(file_path)

# Define the function to scrape top 5 reviews from top critics for a movie URL
def get_top_5_top_critic_reviews(movie_reviews_url):
    try:
        # Send a request to the movie reviews page
        response = requests.get(movie_reviews_url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the reviews based on the inspected HTML structure
        review_elements = soup.find_all('p', class_='review-text')  # Adjust the class accordingly
        top_5_reviews = [review.get_text(strip=True) for review in review_elements[:5]]
        
        # If there are less than 5 reviews, pad the list with empty strings
        while len(top_5_reviews) < 5:
            top_5_reviews.append('')
        
        return top_5_reviews
    except Exception as e:
        print(f"Error fetching reviews for {movie_reviews_url}: {e}")
        return ['', '', '', '', '']

# Function to process each movie
def process_movie(row):
    movie_title = row['title']
    movie_url = row['url']
    movie_reviews_url = f"{movie_url}/reviews?type=top_critics"
    top_reviews = get_top_5_top_critic_reviews(movie_reviews_url)
    
    return {
        'title': movie_title,
        'review_1': top_reviews[0],
        'review_2': top_reviews[1],
        'review_3': top_reviews[2],
        'review_4': top_reviews[3],
        'review_5': top_reviews[4]
    }

# Initialize a list to store the review data
reviews_data = []

# Use ThreadPoolExecutor for parallel processing
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(process_movie, row) for index, row in movie_info.iterrows()]
    for future in as_completed(futures):
        reviews_data.append(future.result())
        time.sleep(1)  # Rate limiting to 1 request per second

# Convert the list of dictionaries to a DataFrame
reviews_df = pd.DataFrame(reviews_data)

# Define the path to save the reviews CSV file
save_path = '/Users/hasaannoor/Desktop/Review Bias Detection/rotten_tomatoes_data_1970_2024/movie_reviews.csv'

# Save the reviews DataFrame to a CSV file
reviews_df.to_csv(save_path, index=False)

# Display the first few rows of the reviews DataFrame to verify
print(reviews_df.head())