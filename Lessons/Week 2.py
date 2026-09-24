'''
Horror/romance
Igor, Shine, freckles
Nuclear Bomb
What path to take?
Who to sacrifice?
Food? Hunt?
'''

Title = "To Be Determined"
path_Left = 100
path_Right = 100

if path_Left <= path_Right:
    shortest_path = "left"

else:
    shortest_path = "right"

print(f'The Shortest path is {shortest_path}')

food_found= input("What kind of food did they find?").lower()
path_taken = input("What path do they take?")
#Python is Case-sensitive
if('nothing' in food_found or path_taken not in shortest_path):
    print("They have a problem")
else:
    print("They should be fine")

who_dies = input("who makes the ultimate sacrifice?")
if (who_dies == "Igor"):
    print("Oh no, poor Igor!")
elif(who_dies== "Shine"):
    print("No! not Shine!")
elif(who_dies == "Freckles"):
    print("You Chose the dog!, How could you!?!")
else:
    print("That wasn't an option. The world ENDS!")
