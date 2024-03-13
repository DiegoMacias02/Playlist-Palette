import openai
from dotenv import load_dotenv
import os
# Assuming 'songs', 'get_lyrics', and 'analyze_sentiment' functions are correctly defined in their respective modules
from song_data import songs
from lyrics_sentiment import get_lyrics, analyze_sentiment

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('openai_api_key')

def generate_summary(songs, overall_sentiment):
    # Generating a song string for the prompt - this part remains unchanged
    song_string = ", ".join([f"{song[0]} by {song[1]}" for song in songs])
    
    # Adjusting the prompt to include overall sentiment obtained from Hugging Face's Transformers
    sentiment_description = "a positive vibe" if overall_sentiment == 'POSITIVE' else "a negative vibe"
    
    prompt = (f"Hello GPT-4, based on a playlist with {sentiment_description}, encapsulate the essence and emotion "
              "without mentioning specific songs or artists. The playlist creates an atmosphere that "
              f"{sentiment_description}, capturing the listener's mood effectively.")
    
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = completions.choices[0].text.strip()
    return summary

def generate_name(summary, used_names):
    prompt = f"Based on this mood: {summary}, suggest a 2-5 word, creative, and unique playlist name."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=32,
        temperature=0.9,  # Adjusted for more creativity
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    name = response.choices[0].text.strip()
    while name in used_names or name == "":
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=32,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )
        name = response.choices[0].text.strip()
    used_names.add(name)
    return name

used_names = set()
names = []

# Example usage - ensure to replace 'overall_sentiment' with actual sentiment analysis result
overall_sentiment = 'POSITIVE'  # Placeholder, use the actual sentiment from lyrics_sentiment.py
summary = generate_summary(songs, overall_sentiment)

for i in range(5):
    name = generate_name(summary, used_names)
    names.append(name)

print("Here are five creative names for your playlist:")
for count, name in enumerate(names, start=1):
    print(f"{count}. {name}")

# User input to choose a name - This part remains unchanged
chosen_name = input("Enter the number of the name you want to select (1-5): ")
while not chosen_name.isnumeric() or int(chosen_name) < 1 or int(chosen_name) > 5:
    chosen_name = input("Enter a valid number from 1-5: ")
chosen_name = names[int(chosen_name) - 1]
