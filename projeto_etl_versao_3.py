import json
import csv

# O arquivo 'friends.json' é um arquivo pessoal disponibilizado pelo aplicativo Snapchat com o histórico completo de "amigos" que foram adicionados ao longo do tempo. 
with open('friends.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

usernames = []

for friend in data["Friends"]:
    if "Username" in friend:
        usernames.append(friend["Username"])

# Ordena os usernames por ordem alfabética
sorted_usernames = sorted(usernames)

# Cria um novo arquivo CSV e escreva os usernames ordenados nele
with open('usernames.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Lista de Amigos (usernames) em ordem Alfabética"])  # Escreva o cabeçalho da coluna
    for username in sorted_usernames:
        csv_writer.writerow([username])  # Escreva cada username em uma linha
