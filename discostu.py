

# snoop a spotify account for currently playing tune.
# identify if the genre is disco and do actions depending on (true, false)

# this is not possible from spotify, we can get a list of genres from the artist only

# to run properly, this must be run where you have a web browser to do the authentication

import json
import spotipy
import webbrowser
import secret
import time
import requests

from pprint import pprint

discoball = "http://disco/switch/lampa/"

print ("Your spotify user name is:",secret.username)


# open with read access to playback state

oauth_object = spotipy.SpotifyOAuth(secret.clientID, secret.clientSecret, secret.redirect_uri, scope="user-read-playback-state")
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To print the response in readable format.
#print(json.dumps(secret.username, sort_keys=True, indent=4))

#forever snoop the currently playing tune

while True:
    track=spotifyObject.current_playback(market="SE")
    #pprint(track)
    #pprint(track["item"]["artists"][0]["id"])
    artid=track["item"]["artists"][0]["uri"]
    artist=spotifyObject.artist(artid)
    #print(artist)
    #print(artist["genres"])

    if "disco" in artist["genres"]:
        r = requests.post(url=discoball+"turn_on")
    else:
        r = requests.post(url=discoball+"turn_off")

    print(r)

    time.sleep(10)
            
