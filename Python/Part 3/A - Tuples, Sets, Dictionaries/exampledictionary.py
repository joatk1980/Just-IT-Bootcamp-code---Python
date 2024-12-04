#each item in a dictionary is a key-value pair (consisting of a key and a value i.e   "Mazda":"Green"
# four elements in my list below(key-value pairs)where "Take That" is key and "Never Forget" is value assigned to it 
#create music playlist 


playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}

#printing the dictionary
print(playlist)

print(playlist["Take That"]) #output: Never Forget

# Add item to the dictionary

playlist["PJ and Duncan"] = "Lets get ready to rhumble"

print(playlist)

# remove dictionary items
playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}

#delete item having "Celeste" key
del playlist["Celeste"]
print(playlist)

#clear the dictionary
playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}
#clear the dictionary
playlist.clear()

print(playlist)

#change dictionay items
playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}

#change value of "Take That" key to "Pray" from "Never Forget"
playlist["Take That"] = "Pray"
print(playlist)

#Iterate through dictionary

playlist = {

#    key            value
    "Gary Barlow": "lead singer",
    "Craig David": "sole vocalist"
}

#print dictionary keys one by one
for singer in playlist:
    print(singer)

print() 

#print dictionary values one by one
for singer in playlist:
    position = playlist[singer]
    print(position)


playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}

#find dictionary length
print(len(playlist))
#result = 4

singer = {}
#get dictionary's length
print(len(singer))
#result 0


playlist = {

 #   key             value
    "Take That": "Never Forget", #element 1
    "Linkin Park": "In the End", #element 2
    "Craig David": "16",
    #element 3
    "Celeste": "Stop this flame"
    #element 4
}


#check whether a key exists in a dictionary by using in and the not in operators

print("Gary Barlow" in playlist) #false
print("Take That" in playlist)#True
print("Gary Barlow" not in playlist) 
#True
