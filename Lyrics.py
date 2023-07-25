import requests
import json

def getLyrics(trackId: str):

    url = f'https://api.lyricstify.vercel.app/v1/lyrics/{trackId}'

    response = requests.get(url)

    # print(response.content.decode('utf-8'))
    json_obj = json.loads(response.content.decode('utf-8'))

    return json_obj["lyrics"]["lines"]