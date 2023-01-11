# Import the Spotipy client and the prompt_for_user_token function from the spotipy.util module
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from dotenv import load_dotenv
import os 

def configure():
    load_dotenv()

configure()

# Replace these with your own client ID and client secret
CLIENT_ID = "cid"
CLIENT_SECRET = "secret"

#Authentication - without user
auth_manager = SpotifyClientCredentials(client_id= os.getenv('CLIENT_ID'), client_secret= os.getenv('CLIENT_SECRET'))

# Replace this with the redirect URI you specified when registering your app
REDIRECT_URI = "http://localhost:8888/callback"

# Request the username from the user
username = input("Enter your Spotify username: ")

# Request authorization to access the user's playlists
scope = "playlist-read-private"
token = util.prompt_for_user_token(username, scope)

# Create a Spotipy client using the authorization token
sp = spotipy.Spotify(auth_manager= SpotifyOAuth())
