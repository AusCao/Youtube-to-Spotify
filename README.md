# YoutubeToSpotify
Imports a Youtube playlist to Spotify. (Only songs that are available on Spotify) <br />
DEMO: <br />
https://www.youtube.com/watch?v=VE2kmldeuBQ <br />

Requirements:  
1. Setup Environment using https://github.com/googleapis/google-api-python-client and https://github.com/plamere/spotipy. 
2. Setup a Spotify developer account at https://developer.spotify.com/documentation/web-api/ and create app with URI set to "http://localhost:8888/callback". 
3. export SPOTIPY_CLIENT_ID="CLIENT_ID" in environment. 
4. export SPOTIPY_CLIENT_SECRET="CLIENT_SECRET" in environment. 
5. export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback" environment. 