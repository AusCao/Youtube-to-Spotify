from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()

# https://developers.google.com/youtube/v3/docs
# https://github.com/googleapis/google-api-python-client

class YoutubePlaylist:

    youtube = build("youtube", "v3", developerKey=os.getenv("API_KEY"))

    def __init__(self, playlistID):
        self.playlistID = playlistID
        self.playlistName = ""
        self.playlist = []
        self.__getPlaylistName()
        self.__getPlaylist()
        

    def __getPlaylistName(self):
        request = self.youtube.playlists().list(part="snippet,contentDetails",
                                               id=self.playlistID)
        response = request.execute()
        self.playlistName = response["items"][0]["snippet"]["title"]

    def __getPlaylist(self):
        request = self.youtube.playlistItems().list(part="snippet,contentDetails",
                                               playlistId=self.playlistID,
                                               maxResults=25)
        response = request.execute()
        while (response != None):
            for item in response["items"]:
                title = item["snippet"]["title"]
                index1 = title.find('(')
                index2 = title.rfind(')')
                if (index1 != -1 and index2 != -1):
                    title = title[0 : index1 : ] + title[index2 + 1 : :]
                index1 = title.find('[')
                index2 = title.find(']')
                if (index1 != -1 and index2 != -1):
                    title = title[0 : index1 : ] + title[index2 + 1 : :]
                index1 = title.find("ft.")
                if (index1 != -1):
                    title = title[0 : index1 : ]
                self.playlist.append(title)
            if ("nextPageToken" in response):
                request = self.youtube.playlistItems().list(part="snippet,contentDetails",
                                            playlistId=self.playlistID,
                                            maxResults=25,
                                            pageToken=response["nextPageToken"])
                response = request.execute()
            else:
                response = None

    def getPlaylist(self):
        return self.playlist
    
    def getPlaylistName(self):
        return self.playlistName
    
    def __del__(self):
        self.youtube.close()




    


    
        