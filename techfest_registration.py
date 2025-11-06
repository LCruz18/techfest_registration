print("Welcome to SMIT TechFest!\nEvent organized by Lindsay Cruz of APPDAET BTCS1")
print("How many participants will register?")
num_participants = int(input())

try:
    if num_participants <= 0: print("Invalid number of participants"), exit()
except ValueError: print("Invalid number of participants"), exit()