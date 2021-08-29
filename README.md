# Youtube-to-Spotify
Imports a Youtube playlist to Spotify. (Only songs that are available on Spotify) <br />
DEMO: <br />
https://www.youtube.com/watch?v=VE2kmldeuBQ <br />

Requirements:  
1. Setup Environment using https://github.com/googleapis/google-api-python-client and https://github.com/plamere/spotipy. 
2. Setup Google API key at https://cloud.google.com/docs/authentication/api-keys.  
3. pip install python-dotenv <br />
4. Setup a Spotify developer account at https://developer.spotify.com/documentation/web-api/ and create app with URI set to "http://localhost:8888/callback". 
5. export SPOTIPY_CLIENT_ID="CLIENT_ID" in environment. 
6. export SPOTIPY_CLIENT_SECRET="CLIENT_SECRET" in environment. 
7. export SPOTIPY_REDIRECT_URI="http://localhost:8888/callback" environment. 
