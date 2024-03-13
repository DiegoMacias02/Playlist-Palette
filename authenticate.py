import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Spotify app credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# Now loading REDIRECT_URI from the environment for flexibility
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:8888/callback')  # Default if not specified

# Expanded scope to include modifying playlists
SCOPES = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'

# Use SpotifyOAuth for authentication which handles token refresh automatically
auth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPES,
                            show_dialog=True)  # show_dialog ensures users are prompted to confirm permissions

# Create a Spotipy client with the auth_manager
sp = spotipy.Spotify(auth_manager=auth_manager)

