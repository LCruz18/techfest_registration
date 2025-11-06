print("Welcome to SMIT TechFest!\nEvent organized by Lindsay Cruz of APPDAET BTCS1")

try:
    num_participants = int(input("How many participants will register?: "))
    if num_participants <= 0: print("Invalid number of participants"), exit()
except ValueError: print("Invalid number of participants"), exit()

participants = [] # list for participants

for i in range(num_participants):
    name = input(f"Enter participant name: ")
    track = input(f"Enter track: ")
    dict_participant = {"name": name, "track": track} # dict for participants
    participants.append(dict_participant)

print("\nRegistered Participants:")
for regis in participants:
    print(f'{regis["name"]} - {regis["track"]}')
