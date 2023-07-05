def leap_year():
    x= input("Enter year: ")
    if int(x)%4==0 and int(x)%100!=0:
        print("Leap Year")
    elif int(x)%100==0 and int(x)%400==0:
        print("Leap Year")
    else:
        print("Non-Leap Year")

leap_year()
