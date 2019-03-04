from random import randint

figures = ["R","P","S"]

random = figures[randint(0,2)]

player = True
while player:
    player = input("(R)ock, (P)aper or (S)cissors?")

    if player == random:
        print("Remis")
    elif player == "R":
        if random == "P":
            print("You Loose")
        else:
            print("You win!!")
    elif player == "P":
        if random == "R":
            print("You win!!!")
        else:
            print("You Loose")
    elif player == "S":
        if random == "R":
            print("You Loose")
        else:
            print("You win")

    again = input("Wanna play again? Y/N")

    if again == "Y":
        player = True
        random = figures[randint(0,2)]
    else:
        player = False
        print("The end")




