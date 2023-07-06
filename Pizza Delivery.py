print("Welcome to Python Pizza Delivery")
size = input("What size of Pizza do you want? S,M,L: ")
add_pepperoni= input("Do you want pepperoni?:Y,N ")
extra_cheese = input("Do you want extra cheese:Y,N ")

small_pizza = int(15)
medium_pizza= int(20)
large_pizza= int(25)

pepperoni_s= int(2)
pepperoni_ml=int(3)

cheese= int(1)

if size == "S":
    if add_pepperoni == "Y" and extra_cheese == "N":
        print(F"Please Pay ${small_pizza+pepperoni_s}")
    elif add_pepperoni=="Y" and extra_cheese=="Y":
        print(f"Please pay $ {small_pizza+pepperoni_s+cheese}")
    elif add_pepperoni=="N" and extra_cheese =="Y":
        print(f"Please pay $ {small_pizza+cheese}")
    else:
        print(f"Please Pay ${small_pizza}")

if size == "M":
    if add_pepperoni == "Y" and extra_cheese == "N":
        print(f"Please Pay ${medium_pizza+pepperoni_ml}")
    elif add_pepperoni=="Y" and extra_cheese=="Y":
        print(f"Please pay $ {medium_pizza+pepperoni_ml+cheese}")
    elif add_pepperoni=="N" and extra_cheese =="Y":
        print(f"Please pay {medium_pizza+cheese}")
    else:
        print(f"Pay ${medium_pizza}")

if size == "L":
    if add_pepperoni == "Y" and extra_cheese == "N":
        print(f"Please Pay ${large_pizza+pepperoni_ml}")
    elif add_pepperoni=="Y" and extra_cheese=="Y":
        print(f"Please pay $ {large_pizza+pepperoni_ml+cheese}")
    elif add_pepperoni=="N" and extra_cheese =="Y":
        print(f"Please pay {large_pizza+cheese}")
    else:
        print(f"Please Pay ${large_pizza}")



