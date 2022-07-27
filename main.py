import random

while True:
    choices = ["pierre", "feuille", "ciseaux"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Choisissez entre pierre, feuille ou ciseaux : ").lower()

    if player == computer:
        print("computer", computer)
        print("player", player)
        print("Egalité !")
    elif player == "pierre":
        if computer == "feuille":
            print("computer", computer)
            print("player", player)
            print("Vous avez perdu !")
        else:
            print("computer", computer)
            print("player", player)
            print("Vous avez gagné !")
    elif player == "ciseaux":
        if computer == "pierre":
            print("computer", computer)
            print("player", player)
            print("Vous avez perdu !")
        else:
            print("computer", computer)
            print("player", player)
            print("Vous avez gagné !")
    elif player == "feuille":
        if computer == "ciseaux":
            print("computer", computer)
            print("player", player)
            print("Vous avez perdu !")
        else:
            print("computer", computer)
            print("player", player)
            print("Vous avez gagné !")

    play_again = input("Voulez-vous jouer à nouveau ? (o/n) : ").lower()

    if play_again == "n":
        break
print("Au revoir !")