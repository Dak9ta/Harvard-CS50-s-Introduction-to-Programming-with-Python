import json
import requests
import sys

# you can use the sys package, but I prefer it like this
artist = input("What artist would you like to search: ")
    
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + artist)
#print(json.dumps(response.json(), indent=2)) # this is for printing all of the specs of a song
# this is for printing only the name of the song
o = response.json()
for result in o["results"]:
    print(result["trackName"])