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
    prompt = f"Summarize in 2-4 very descriptive and creative sentences, the underlying rhythmic style/groove, mood and feel of these songs in a playlist, make sure to NOT USE ANY OF THE SONG NAMES OR ARTIST NAMES' IN THE SUMMARY. This playlist contains the following songs (make sure these 2-4 sentences encapsulates the entire feeling someone would recieve when listening to this playlist): {song_string}"
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

#summary of the songs
summary = generate_summary(songs)

#prompt to feed to gtp-3
prompt_summary = f"Hello I am working on a project to make playlist-name recommendation to users based on their songs in their playlist."                     
+"I need you to give me one name that you believe fits this playlist and that is it nothing else in the text-response(because I am"
+" using you as an api call currently) you give (Do not include the title, or any words from the tile of any the songs, or any of aritist name in the response)"
+ "Give me a creative, unique, quirky, and aesthetic name that encapsulates the overall vibe of the following songs, only" 
+f"respond with a 1-5 word name for this playlist and nothing else. Here is a summary GTP-3 came up with about the songs: {summary}. " 
+"Please provide me with a 1-5 word response on what you believe is a creative, quirky, and asthetic name that fits this summary."

#generates "playlist-names" based on a summary created by gtp-3 of a user's playlist songs
def generate_name(summary, used_names):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=summary,
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
            prompt = summary,
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
    name = generate_name(prompt_summary, used_names)
    names.append(name)
    used_names.append(name)

print("Here are five creative names for your playlist:")
for count, name in enumerate(names, start=1):
    print(count, name)

chosen_name = input("Enter the number of the name you want to select (1-5): ")
chosen_name = names[int(chosen_name) - 1]
