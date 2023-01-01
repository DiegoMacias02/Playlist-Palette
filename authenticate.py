import spotipy
import spotipy.util as util

# Replace these with your own client ID and client secret
CLIENT_ID = "e459f05bbb634aacb779c08530c4d26f"
CLIENT_SECRET = "6858abef8c7e4b91b938e0af2d7725eb"

# Replace this with the redirect URI you specified when registering your app
REDIRECT_URI = "http://localhost:8888/callback"

# Replace this with the username of the user you want to authenticate
USERNAME = input("Enter your Spotify username: ")

# Request authorization to access the user's playlists
scope = "playlist-read-private playlist-read-collaborative"
token = util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

# Create a Spotipy client using the authorization token
sp = spotipy.Spotify(auth=token)

# Test the client by retrieving the user's playlists
playlists = sp.user_playlists(USERNAME)
print(playlists)
