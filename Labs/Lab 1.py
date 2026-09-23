'''
#Steps 1-3
answer1= 5+3
answer2= 7*4
print("answer1")
print(answer1)

print("answer2")
print(answer2)
'''

#Steps 4 Onward
x = 7
print(x)
y = x+5
# The following prints using the format function
print("x is {} and y is {}".format(x,y))
# The following prints using the interpolation method
print("x is %d and y is %d" %(x,y))

shopName = input("Please enter the shop name: ")
ringQTY = int(input("Please enter the ring QTY: "))
glassesQTY = int(input("Please enter the glass QTY: "))
print("Shop name is {}".format(shopName))
print("Ring QTY is {}".format(ringQTY))
print("Glass QTY is {}".format(glassesQTY))

print("Inventory Total: {}" .format(ringQTY+glassesQTY))
