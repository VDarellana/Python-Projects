#Donut shop
#Donuts
#Coffee
#Other Beverages
#Music
#Customers
#Other Baked goods
#Employees

#Frank's Finest

typeOfShop = 'Donut Shop'
shopName = "Frank's Finest"
SLOGAN = "Frank's fantastic fritters"

donuts_sold = 0
donutsSellPrice = 0.50

#Two Different ways of printing a program out with two string variables together
#Method #1 - Plus Signs (Double quotes with a space is needed)
print(shopName + " " + typeOfShop)
#Method #2 - Comma will do the same thing of printing two variables
print(shopName,typeOfShop)

donuts_sold =  float(input("how many donuts sold?: "))
revenue = donuts_sold * donutsSellPrice
#Formating
print("You sold donuts %d and now made %.2f " %(donuts_sold,revenue))
print(SLOGAN.endswith("fritters"))
print(SLOGAN.find("fantastic"))
print(SLOGAN[0:5])
#.endswith() - This statement is a Boolean checker that checks if your variable has a certain word to satisfy a condition
'''
print( f"You sold donuts {donuts_sold} and now made {revenue} ")
'''
#.find() -  Statement that tells you when a word starts in a sentence