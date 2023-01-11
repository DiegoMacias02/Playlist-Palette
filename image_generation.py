import openai
import requests
from PIL import Image
from io import BytesIO
import os 
from dotenv import load_dotenv
from song_data import songs, selected_name
#run this to get env
load_dotenv()
# Replace this with your own API key
openai.api_key = os.getenv('openai_api_key')

# Prompt the user to enter the art style
art_style = input("Enter the art style you want to use for your playlist image "
                    + "(e.g. 'watercolor', 'oil', 'graffiti', etc.): ")

# Define a function to generate a summary of the playlist using GPT-3
def generate_summary(songs, selected_name, art_style):
    song_string = " ".join([f"{song[0]} by {song[1]}" for song in songs])
    prompt = f"Summarize the overall vibe, mood and feel of playlist named {selected_name} containing following songs in a few words, also mention the art style you want to use in the summary(this is going to used as a request for dalle-2 so make it as best fit for that): {song_string} {art_style}"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=128,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message

# Define a function to generate an image using DALL-E 2 based on the summary
def generate_image(summary):
    response = openai.Image.create(
        prompt=f"generate an image based on this summary: {summary}",
        n=1,
        size="1024x1024"
    )
    url = response.data[0]["url"]
    return url

# Get the url of the image
url = generate_image(generate_summary(songs, selected_name, "abstract"))

# Open the image and show it
image = Image.open(BytesIO(requests.get(url).content))
image.show()

