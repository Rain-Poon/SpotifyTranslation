import spotipy

def get_current_line_of_lyrics():
  """Gets the current line of lyrics playing on Spotify."""

  client = spotipy.Spotify(auth_token="BQDVHqQDhLhxV18igB03n_B44yPP9CnCCuIOAMEsXKhgs07ctxufLpTdruTG0M3z9jmj2KnpEv7Pm_LfY5OuszmXB-cLyI1o4-AHeuH-fRIgB4MXII76pplf7GYoHL7rwk8-_pRmYJZaAXUSPJVLgz7EuYXrg-3NVedr5qW-6Ph6W4_k2Bk6Y_ebX5yOZLRIjq4fvvNNt7pZMuL2Gx8GiobU")
  current_song = client.current_playing()
  lyrics = current_song["track"]["lyrics"]
  line_number = int(current_song["progress_ms"] / 1000 / 60 / 100)
  return lyrics[line_number]

if __name__ == "__main__":
  line_of_lyrics = get_current_line_of_lyrics()
  print(line_of_lyrics)
