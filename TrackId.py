import requests
import json
from datetime import datetime

def getTrackId(access_token: str):
    url = 'https://api.spotify.com/v1/me/player/currently-playing'

    headers = {
        'Authorization': f'Bearer {access_token}' 
    }

    response = requests.get(url, headers=headers)
    
    millis = int(datetime.utcnow().timestamp() * 1000)

    json_obj = json.loads(response.content)

    return json_obj["item"]["id"], json_obj["progress_ms"], json_obj["item"]["duration_ms"], millis