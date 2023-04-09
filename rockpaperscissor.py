import random

choice =["rock","paper","scissor"]

computer=random.choice(choice)


player=None

while player not in choice:
    player=input("rock,paper or scissor:").lower()
    if player not in choice:
        print("Invalid input try again")

if player == computer:
    print("compurter: ",computer)
    print("player:",player)
    print("Tie!")
elif player == "rock":
    if computer =="paper":
        print("computer:",computer)
        print("player:",player)
        print("computer wins")
    elif computer=="scissor":
        print("computer:", computer)
        print("player:", player)
        print("player wins")
elif player == "paper":
    if computer =="scissor":
        print("computer:", computer)
        print("player:", player)
        print("computer wins")
    elif computer =="rock":
        print("computer:", computer)
        print("player:", player)
        print("computer wins")
elif player =="scissor":
    if computer=="rock":
        print("computer:", computer)
        print("player:", player)
        print("computer wins")
    elif computer =="paper":
        print("computer:", computer)
        print("player:", player)
        print("player wins")