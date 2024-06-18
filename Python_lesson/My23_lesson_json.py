import json
filename = "user_settings.txt"
myfile = open(filename, 'w', encoding='utf-8')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "Ny"]
}    

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}   

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#--------save by json-----------
json.dump(myplayers, myfile)
myfile.close()

# -------load by JSON-----------

myfile = open(filename, 'r', encoding='utf-8')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award №1: " + str(user['awards'][0]))
    print("Player Award №2: " + str(user['awards'][1]))
    print("Player Award №3: " + str(user['awards'][2]))
          
    print("--------------------------------\n\n")
