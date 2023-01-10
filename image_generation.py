# Import the necessary libraries
import requests
from requests.structures import CaseInsensitiveDict

import json

# Replace these values with your own Dall-E 2 API key and model
API_KEY = "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"
MODEL = "image-alpha-001"

# Define the endpoint URL
ENDPOINT = "https://api.openai.com/v1/images/generations"

# Define the headers
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = f"Bearer {API_KEY}"

# Define the data to send in the request
data = """
{
    """

# Add the model to use
data += f'"model": "{MODEL}",'

# Add the prompt
prompt = "Generate an image that captures the overall theme and vibe of this playlist with the name " + selected_name
data += f'"prompt": "{prompt}",'

# Add the number of images to generate
data += """
    "num_images":1,
    "size":"1024x1024",
    "response_format":"url"
}
"""

# Send the request
response = requests.post(ENDPOINT, headers=headers, data=data)

# Check the status code
if response.status_code != 200:
    raise ValueError("Failed to generate image")

# Print the image URL
image_url = response.json()["data"][0]["url"]
print(f"Image URL: {image_url}")

# Download the image and save it to a file
urllib.request.urlretrieve(image_url, "playlist_image.jpg")
