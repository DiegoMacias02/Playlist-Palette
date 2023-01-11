# Import the Spotipy client and the prompt_for_user_token function from the spotipy.util module
import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from dotenv import load_dotenv
import os 

#load enviroment 
load_dotenv()

#ID's for accessing api
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

#Authentication - without user
#auth_manager = SpotifyClientCredentials(client_id= os.getenv('CLIENT_ID'), client_secret= os.getenv('CLIENT_SECRET'))

# Replace this with the redirect URI you specified when registering your app
REDIRECT_URI = "http://localhost:8888/callback"

# Request the username from the user
username = input("Enter your Spotify username: ")

# Request authorization to access the user's playlists
scope = "playlist-read-private playlist-read-collaborative"
token =  util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

# Create a Spotipy client using the authorization token
sp = spotipy.Spotify(auth = token)
