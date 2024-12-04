playlistv1 = {
    "title":"Never Forget",
    "artist":"Take That",
    "genre":"Pop",
    "year": 1996


}

# allows you to enter a new record by prompting user to enter a new record 
print(f"Playlistv1: {playlistv1}")
for aKey in playlistv1
    playlistv1[aKey] = input(f"Enter value for {aKey}: ")

# to have multiple songs in a dictionary we have to use nesting - a dictionary can contain dictionaries this is called nested dictionaries 

playlistv2 = {
"song1":{ "artist":"Mr Beat", "genre":"Pop", "song_year":2012}
"song2":{ "artist":"Take That", "genre":"Pop", "song_year":1996}
"song3":{ "artist":"Michael Jackson", "genre":"Pop", "song_year":1990}
"song4":{ "artist":"Tupac", "genre":"Rap", "song_year":1993}
"song5":{ "artist":"Jay Z", "genre":"Grime", "song_year":1995}



}

print(playlistv2)

print(f"Playlist2: {playlistv2["song2"]}") #will tell you what song2 is
print(f"Playlist2:  {playlistv2["song3"]["artist"]}")

for songs in playlistv2: #will print the name of the songs 
    print(songs)

for songs,data in playlistv2.items():
    print(songs,data)  

for song_keys in playlistv2.keys():
    print(song_keys)        #will show list of keys 

for song_vals in playlistv2.values():
    print(song_vals)        #will show values not the keys 