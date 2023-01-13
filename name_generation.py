import openai
from song_data import songs
from dotenv import load_dotenv
import os

#loading in from my os
load_dotenv()
openai.api_key = os.getenv('openai_api_key')

# Define a function to generate a summary of the playlist using GPT-3
def generate_summary(songs):
    song_string = " ".join([f"{song[0]} by {song[1]}" for song in songs])
    prompt = f"Hello GPT-3, I am currently using you as an API call for a project where I am creating playlist name recommendations for users based on their songs. I need you to summarize in 2-4 very descriptive and creative sentences, the underlying rhythmic style/groove, mood and feel of these songs. It is important that the summary encapsulates the entire feeling someone would receive when listening to these songs, DO NOT INCLUDE ANY OF THE SONG NAMES OR ARTIST NAMES in the summary. The following songs: {song_string}. Can you please provide me with a summary that accurately captures the essence/emotion of this? Also do not mention that it any songs or even that what you are summarizing are songs!"
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

#generates "playlist-names" based on a summary created by gtp-3 of a user's playlist songs
def generate_name(summary, used_names):
    prompt = f"Please provide a 2-5 word, creative, fun, quirky, and unique name for a playlist based on the following summary of the playlist: {summary}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=32,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )
    name = response.choices[0].text.strip()
    while name in used_names:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=32,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=0.3,
            presence_penalty=0.3
        )
        name = response.choices[0].text.strip()
        used_names.add(name)
    return name


used_names = set()
names = []

#summary of the songs
summary = generate_summary(songs)

for i in range(5):
    name = generate_name(summary, used_names)
    names.append(name)

print("Here are five creative names for your playlist:")
for count, name in enumerate(names, start=1):
    print(count, name)

chosen_name = input("Enter the number of the name you want to select (1-5): ")
while not chosen_name.isnumeric():
    chosen_name = input("Enter a valid number from 1-5: ")

chosen_name = names[int(chosen_name) - 1]
