#Name - Victor Daniel Arellana Assia
#Student ID -251522305
#Date - September 22nd 2025 - 09/22/2025
#Course - Computer science 1026

#Purpose - Code outputs calculation of the final amount of fuel that
# is wanted by receiving Input of fuel type and fuel amount and
# uses predetermined cost values per litre inputted by user


#User Input Fuel Type + declaring extra variables
charFuel = False
amountFuel = 0.0
finalCost = 0.0
typeAns = False
fuelType = input("Select fuel type: ").lower().replace(" ","")
#First If Statement checking fuel type is correct
if fuelType == "regular" or fuelType == "extra" or fuelType == "premium" or fuelType == "diesel" :
    typeAns = True
    amountFuel = input("Enter the amount of fuel you want: ").replace(" ", "")
    #Checks all rules of and verify if input is a valid reason
    if amountFuel.count(".") == 1 and amountFuel.isalpha() == False and amountFuel[amountFuel.find(".")+ 1:].isdigit() == True and amountFuel[:amountFuel.find(".")].isdigit()  == True:
        charFuel = True
        amountFuel = float(amountFuel)
else:
    #prints invalid fuel type if wrong answer inputted
    print("invalid fuel type")

#Checks if amount of fuel is valid
if (charFuel == False or amountFuel <= 0)and typeAns == True:
    print("invalid number of litres of fuel")
else:
    # calculates the final cost depending on the fuel selected
    #Cost of each fuel type is immediately calculated
    if fuelType == "regular":
            finalCost = round(amountFuel * 1.42,2)
            # prints out final cost
            print("Cost: $" + str(finalCost))
    elif fuelType == "extra":
            finalCost = round(amountFuel * 1.53,2)
            # prints out final cost
            print("Cost: $" + str(finalCost))
    elif fuelType == "premium":
            finalCost = round(amountFuel * 1.60,2)
            # prints out final cost
            print("Cost: $" + str(finalCost))
    elif fuelType == "diesel":
            finalCost = round(amountFuel * 1.75,2)
            # prints out final cost
            print("Cost: $" + str(finalCost))