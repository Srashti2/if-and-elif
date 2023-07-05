print("Welcome to the rollercoaster")
height = int(input("What is your height in cm"))
age = int(input("What is your age?: "))
photos = input("would you like to have photos then it would cost more upto 3$? y or n: ")
if height >= 120 and age <12 :
    print("You can ride ")
    if photos =="y":
        print("You need to pay $8")
    else:
        print("You can ride, Please pay $5")
elif height>=120 and 12<=age<18:
    print("You can ride ")
    if photos=="y":
        print("You need to pay $10")
    else:
        print("You can ride, Please pay $7")
elif height>=120 and age>=18:
    print("You are elegible to ride")
    if photos == "y":
        print("You can ride, Please pay $15")
    else:
        print("You can ride please pay $12")
else:
    print("You cannot ride")






