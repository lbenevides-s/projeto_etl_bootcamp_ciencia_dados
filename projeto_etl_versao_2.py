import json 

with open('friends.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

usernames_with_timestamp = []

for friend in data["Friends"]:
    if "Username" in friend and "Creation Timestamp" in friend:
        username = friend["Username"]
        creation_timestamp = friend["Creation Timestamp"]
        usernames_with_timestamp.append((username, creation_timestamp))

usernames_tuple = tuple(usernames_with_timestamp)
print(usernames_tuple)
