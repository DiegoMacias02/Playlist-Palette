import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from transformers import pipeline

# Load the environment variables from the .env file
load_dotenv()

def get_lyrics(song_name, artist_name):
    # Genius API endpoint
    url = "https://api.genius.com/search"
    api_token = os.getenv('GENIUS_API_TOKEN')

    # Parameters for the API request
    params = {
        'q': f"{song_name} {artist_name}"
    }

    # Headers for the API request
    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    # Send the request
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Get the URL of the first song in the results
    song_url = data['response']['hits'][0]['result']['url']

    # Send a request to the song URL
    response = requests.get(song_url)
    response.raise_for_status()

    # Parse the HTML response to extract the lyrics
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics = soup.find('div', class_='lyrics').get_text()

    return lyrics

# Initialize the sentiment analysis pipeline from Hugging Face's Transformers
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the provided text using Hugging Face's Transformers.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple: A tuple containing the sentiment label ('POSITIVE' or 'NEGATIVE') and the confidence score.
    """
    # Perform sentiment analysis on the text
    result = sentiment_pipeline(text)

    # Extract the sentiment and confidence score from the result
    sentiment = result[0]['label']
    score = result[0]['score']

    # Return the sentiment label and score
    return sentiment, score
