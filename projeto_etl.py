import json 

with open('friends.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

#total_friends = len(data["Friends"])
#print(f"Total de amigos: {total_friends}")

for friend in data["Friends"]:
    if "Username" in friend:
       print(friend["Username"])