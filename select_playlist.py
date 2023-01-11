# Import the Spotipy client
import spotipy
from authenticate import sp, username
# Retrieve the user's playlists
playlists = sp.user_playlists(username)

# Print the name and ID of each playlist
for playlist in playlists["items"]:
    print(f"{playlist['name']}")

# Prompt the user to select a playlist
selected_name = input("Enter the name of the playlist you want to select: ")
selected_id = None

# Loop through the playlists and check if the name entered by the user matches the name of any of the playlists
for playlist in playlists["items"]:
    if playlist["name"] == selected_name:
        selected_id = playlist["id"]
        break

if selected_id is not None:
    print(f"Selected playlist: {selected_name, selected_id}")
else:
    print("Playlist not found.")
