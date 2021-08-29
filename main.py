import youtube_playlist as yp
import spotify_playlist as sp


if __name__ == '__main__':
    # Test playlist: PLw-VjHDlEOgs658kAHR_LAaILBXb-s6Q5
    username = input("Enter spotify username: ")
    
    #playlistID = "PLw-VjHDlEOgs658kAHR_LAaILBXb-s6Q5"
    
    while (True):
        playlistID = input("Enter playlist ID: ")
        youtubePlaylist = yp.YoutubePlaylist(playlistID)
        playlistName = youtubePlaylist.getPlaylistName()
        tracklist = youtubePlaylist.getPlaylist()
        spotify = sp.SpotifyPlaylist(username)
        spotify.createPlaylist(playlistName, tracklist)
        done = input("Do you want to create more playlists? (y/n): ")
        if (done == "n"):
            break
