n = int(input("How many numbers do you want to use today?: "))
if n>0:
    firstValue = int(input("Enter first number: "))
    smallest = firstValue
    largest = firstValue
    total = firstValue

    counter = 0
    while counter <(n-1):
        current = int(input("Enter you next number: "))
        total = total + current
        counter += 1
        if current < smallest:
            smallest = current
        elif current > largest:
            largest = current

    print("The average of the value is: ", total/n)
    print("The smallest number is: {}".format(smallest))
    print("The largest number is: {}".format(largest))
    print("The range of the value is {}".format(largest-smallest))
else:
    print("You did not want to use a number today.")

#part 2

accountTotal = 50
while accountTotal >= 20:
    print(accountTotal)
    accountTotal-= 1
print("Your balance has reached $20!")