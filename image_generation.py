import openai
import requests
from PIL import Image
from io import BytesIO
import os 
from dotenv import load_dotenv
from song_data import songs
from name_generation import chosen_name, summary

#run this to get env
load_dotenv()
# Replace this with your own API key
openai.api_key = os.getenv('openai_api_key')

# Prompt the user to enter the art style
art_style = input("Enter the art style you want to use for your playlist image "
                    + "(e.g. 'watercolor', 'oil', 'graffiti', etc.): ")

# Define a function to generate an image using DALL-E 2 based on the summary
def generate_image(summary):
    response = openai.Image.create(
        prompt=f"generate an image based on this summary with this style of imagery {art_style}: {summary}",
        n=1,
        size="1024x1024"
    )
    url = response.data[0]["url"]
    return url

print(summary)
# Get the url of the image
url = generate_image(summary)

# Open the image and show it
image = Image.open(BytesIO(requests.get(url).content))
image.show()

