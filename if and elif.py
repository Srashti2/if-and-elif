print("Welcome to the rollercoaster")
height = int(input("What is your height in cm"))
age = int(input("What is your age?: "))
if height >= 120 and age >18:
    print("You can ride and you have to pay $12")
elif height>=120 and age <=18:
    print("You can ride and you are elegible to pay  $7")
else:
    print("You cannot ride")




