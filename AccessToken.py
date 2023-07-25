import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "5b2a75db113f426db7fe8683fe69a37f"
SPOTIPY_CLIENT_SECRET = "99d4a3d4aa17426fba6afaebb27144cc"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

# Get auth url
auth_url = sp_oauth.get_authorize_url()
print(auth_url)

# Get auth token from url
code = sp_oauth.parse_response_code(auth_url) 
print("Code: ", code)
token_info = sp_oauth.get_access_token(code)
print(token_info)

# Create spotify object
token = token_info['access_token']
sp = spotipy.Spotify(auth=token)

# Get user info
sp.current_user()