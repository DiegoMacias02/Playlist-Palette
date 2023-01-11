import openai
from song_data import songs
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('openai_api_key')

def generate_name(songs, used_names):
    song_string = " ".join([f"{song[0]} by {song[1]}" for song in songs])
    prompt = f"(Do not include the title (or any words from the tile) of any the songs or any of aritist name in the response) Give me a creative, unique, quirky, and aesthetic name that encapsulates the overall vibe of the following songs, only respond with a 1-5 word name for this playlist and nothing else:\n{song_string}"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=32,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )
    name = response["choices"][0]["text"]
    while name in used_names:
        response = openai.Completion.create(
            model="text-curie-001",
            prompt = f"(Do not include the name of any the songs or any of aritist in the response) Give me a new, creative, unique and aesthetic name that encapsulates the overall vibe of the following songs, only respond with a 1-5 word name for this playlist and nothing else:\n{song_string}",
            max_tokens=32,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0.3,
            presence_penalty=0.3
        )
        name = response["choices"][0]["text"]
    return name

used_names = []
names = []
for i in range(5):
    name = generate_name(songs, used_names)
    names.append(name)
    used_names.append(name)

print("Here are five creative names for your playlist:")
for count, name in enumerate(names, start=1):
    print(count, name)

selected_name = input("Enter the number of the name you want to select (1-5): ")
selected_name = names[int(selected_name) - 1]
