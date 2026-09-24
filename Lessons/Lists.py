'''
4,10,105,3,and 6
eye surgery
it's cool
infection
hangover
'''

guesses = [4,10,105,3,6]
print(f"The guesses were: {guesses}")
print(f"we made {len(guesses)} guesses")
print(f"The first guess was {guesses[0]}")
print(f"the sum of all the guesses is {sum(guesses)}") #Sum(statement)
new_list = [0] * 5
print(new_list)
"""
first_guess = 'eye surgery'
print(f"The first guess was {first_guess}")
first_guess[0] = "E"
print(f"The first letter of that is {first_guess[0]}")
"""

reasons = ['hungover','eye glasses',"its cool", 'infection']
print(f"The reasons were : {reasons}")
reasons.pop(0) #-1 will choose the last item in the list also must be in the range of the list
#.pop() removes an item in a list
search = input("which reason to search for?")

if search.lower() in reasons:
    print(f"{search} was found in our list")
    found_at = reasons.index(search) #Index searches for the item in a list or string and gives a value in return
    print(f'{search} at index {found_at}')
    reasons.pop(found_at)
    reasons.remove(search.lower())
else:
    print(f"{search} was not found in our list")
reasons.sort()
print(f'in th end, the reasons were: {reasons}')

#A list in a list
table  = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f'The entire table is{table}')
print(f'the second row is {table[1]}')
print(f'The third item of the second row{table[1][2]}')
"""

done = False
while not done:
    reason = input("why is mike wearing sunglasses?")
    if reason == '':
        done = True
    else:
        #reasons.append(reason)
        reasons.insert(0, reason)
print(f"The reasons were: {reasons}")

#Number Case in Iclicker
nums = []
for i in range(7):
    if i % 2 == 0:
        nums.append(i)
    else:
        nums.insert(0, i)
print(nums)
"""