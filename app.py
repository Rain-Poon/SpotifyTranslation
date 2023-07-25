from googletrans import Translator
from TrackId import getTrackId
from Lyrics import getLyrics
from datetime import datetime
import time

translator = Translator()

# trackId, progress, duration, getTime = getTrackId(access_token="BQCoQvobo3JPqlYQOASuGSQVbzDtpX6QbQ41oBeVP5N0WKNCyLYNHZYOIPC9U22VEHjw8SalbFvndT_KJx8FvBrvpAEoM71Jv7oY9IiYoRtXofGaaibxDSRwHNlyUa9YfH_ANrVUIMSwzYS7raNOWlsivPmolAc3kqBoMb4mq-4JocEn2ZmAFVCt--EDXB9pKE0OMBgpar-rUoPCkDp3O-1f")

# lyrics = getLyrics(trackId)
# prev_time = getTime
# shown_line = ""
# while (progress < duration):
#     for line in lyrics:
#         if line["startTimeMs"] > progress:
#             break
#         prev_words = line["words"]
#     if (prev_words != shown_line):
#         print(progress)
#         print(prev_words)
#         translated_text = translator.translate(prev_words, dest='en').text
#         print(translated_text)
#         print()
#         shown_line = prev_words
#     time.sleep(1)
#     progress += int(datetime.utcnow().timestamp() * 1000) - prev_time
#     prev_time = int(datetime.utcnow().timestamp() * 1000)

prev_trackId = ""
while (True):
    trackId, progress, duration, getTime = getTrackId(access_token="BQBTobyKjwB3UjTwKW5juyTVpbMLyktGWwcO1PE92Hx-ebyocbuDo-OeidPP9Jh_N3L4qRb72TQD_QXcJ66Kdwp6VlRkKI6mxaDBZoo4ShI5rWgS1SghP0Ss_7vX_-g8fqxgseiVIaQ730WcJ-hb_GbX3uu4EXkd4tVgItb0DCmn_d0JqBBujjsRltNDakybaTFLSv-j99wre9bvXUy3G-sF")
    if (trackId != prev_trackId):
        prev_trackId = trackId
        lyrics = getLyrics(trackId)
        for line in lyrics:
            if line["startTimeMs"] > progress:
                break
            prev_words = line["words"]
        print(prev_words)
        translated_text = translator.translate(prev_words, dest='en').text
        print(translated_text)
        print()
        shown_line = prev_words
    else:
        for line in lyrics:
            if line["startTimeMs"] > progress:
                break
            prev_words = line["words"]
        if (shown_line != prev_words):
            print(prev_words)
            translated_text = translator.translate(prev_words, dest='en').text
            print(translated_text)
            print()
            shown_line = prev_words
    time.sleep(0.5)