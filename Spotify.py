import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials(
        client_id='ed6e7dd16fcb4be684cd1fb8d7a454e5',
        client_secret='b41d895bd0a04fb8ac287e46da493cce')

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = spotify.current_user_playing_track()
results = track['item']['name']
print(results)


# User ID: 11121353752
