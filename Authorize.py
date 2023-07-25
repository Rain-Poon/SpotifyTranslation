import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# start the server by running Server.py first

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

scope = "user-read-currently-playing"

sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=scope)

# Get auth url
auth_url = sp_oauth.get_authorize_url()
print(auth_url) 

# Opens auth url in browser
import webbrowser 
webbrowser.open(auth_url)

# Get auth token from url
code = sp_oauth.parse_response_code(input("Paste the callback url: "))
token_info = sp_oauth.get_access_token(code)

token = token_info['access_token']
print(token)