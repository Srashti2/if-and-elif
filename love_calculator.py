print("Welcome to love calculator")
name1= input("What is your name? \n")
name2= input("What is their name? \n")
print(type(name1))
print(type(name2))

#count function does not count upper case characters
name1_l = name1.lower()
name2_l= name2.lower()

true_count =  name1_l.count("t")+name1_l.count("r")+name1_l.count("u")+name1_l.count("e")+name2_l.count("t")+name2_l.count("r")+name2_l.count("u")+name2_l.count("e")
love_count = name1_l.count("l")+name1_l.count("o")+name1_l.count("v")+name1_l.count("e")+name2_l.count("l")+name2_l.count("o")+name2_l.count("v")+name2_l.count("e")

print(true_count*10)
print(love_count)

#if less than 50%, find someone else
#if greater than 50, you are like coke and mentos

love_point= true_count*10+love_count
print(type(love_point))

if love_point<=50:
    print(f'find someone else, your love score is {love_point}')
else:
    print(f"you are like mentos and coke your love score is {love_point}")