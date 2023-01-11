# Import the OpenAI API client
import openai
#import songs from selected playlist 
from PlaylistPlatte.song_data import songs
# Replace this with your own API key
openai.api_key = "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"

# Define a function to generate a name for the playlist using ChatGPT
def generate_name(songs, used_names):
    # Join the names and artists of the songs into a single string
    song_string = " ".join([f"{song[0]} by {song[1]}" for song in songs])

    # Use ChatGPT to generate a name for the playlist based on the song data
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"(Do not include the name of any the songs or any of aritist in the response) Give me an interesting name that encapsulates the overall vibe of the following songs, only respond with a 1-5 word name for this playlist and nothing else:\n{song_string}",
        max_tokens=32,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated name from the response
    name = response["choices"][0]["text"]

    # If the name has already been used, generate a new name
    while name in used_names:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"I previously asked you to generate an interesting name for a playlist containing these songs and you told me the name {name}. Now I want you to give me a new name with the same songs to encapsulates the over vibe of these songs, only respond with a 1-5 word name for this playlist and nothing else (Do not include the name of any the songs or any of aritist in the response):\n{song_string}",
            max_tokens=32,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        name = response["choices"][0]["text"]

    return name

# Initialize a list of used names
used_names = []

# Generate a list of five names for the playlist
names = []
for i in range(5):
    name = generate_name(songs, used_names)
    names.append(name)
    used_names.append(name)

# Print the generated names
print("Here are five creative names for your playlist:")
for count, name in enumerate(names, start=1):
    print(count, name)

# Prompt the user to select a name
selected_name = input("Enter the number of the name you want to select (1-5): ")

# Save the selected name
selected_name = names[int(selected_name) - 1]
