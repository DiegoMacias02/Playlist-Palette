from authenticate import sp
from select_playlist import selected_id
# Retrieve the selected playlist
try:    
    selected_playlist = sp.playlist(selected_id)
except: 
    print("Invalid Playlist Id")

# Extract the names and artists of the songs in the playlist
songs = []
for item in selected_playlist["tracks"]["items"]:
    song = item["track"]
    name = song["name"]
    artist = song["artists"][0]["name"]
    songs.append((name, artist))
