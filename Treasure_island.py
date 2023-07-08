print("Welcome to Treasure Island, Your mission is to find the treasure island")


left_right =input("Please choose if you want to go left or right: \n")
if left_right == "left":
    swim_wait=input("please choose if you want to swim or wait: \n")
    if swim_wait=="wait":
        which_door= input("please choose which door red, blue or yellow: \n")
        if which_door== "red":
            print("Burned by fire. Game over.")
        elif which_door=="blue":
            print("Eaten by beasts.Game over")
        elif which_door=="yellow":
            print("You won")
        else:
            print("Game Over")
    else:
        print("attacked by trout.Game Over")
else:
    print("Fall into a hole Gameover")

