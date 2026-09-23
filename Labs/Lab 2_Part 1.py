Age =int(input("Enter Age in  years: "))
if Age >= 9 :
    Height =int(input("Enter Height in cm: "))
    if Height > 130 :
        print("you can go on the ride !")
    else :
        print("you are too short for this ride!")
else:
    print("you are too young for this ride")