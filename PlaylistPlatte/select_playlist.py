# Import the Spotipy client
import spotipy
from PlaylistPlatte.authenticate import sp, username
# Retrieve the user's playlists
playlists = sp.user_playlists(username)

# Print the name and ID of each playlist
for playlist in playlists["items"]:
    print(f"{playlist['name']} ({playlist['id']})")

# Prompt the user to select a playlist
selected_id = input("Enter the ID of the playlist you want to select: ")