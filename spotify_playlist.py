import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

# https://github.com/plamere/spotipy

class SpotifyPlaylist:

    def __init__(self, username):
        #self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"),
                                                            # client_secret=os.getenv("CLIENT_SECRET"),
                                                            # redirect_uri=os.getenv("REDIRECT_URI"),
                                                            # scope="playlist-modify-public"))
        token = spotipy.util.prompt_for_user_token(username, scope="playlist-modify-public", show_dialog=True)
        self.sp = spotipy.Spotify(token)

        self.username = username
    
    def createPlaylist(self, playlistName, playlist):
        self.sp.user_playlist_create(self.username, name=playlistName)
        userPlaylists = self.sp.user_playlists(self.username)
        playlistID = userPlaylists["items"][0]["id"]
        for song in playlist:
            result = self.sp.search(q=song)
            if (len(result["tracks"]["items"]) >  0):
                songURI = [result["tracks"]["items"][0]["uri"]]
                self.sp.playlist_add_items(playlistID, songURI)

