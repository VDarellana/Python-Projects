import turtle as t
from dice import roll_dice

dice1 = roll_dice()
dice2 = roll_dice()

if dice1 == dice2:
    print("Yahtzee!")
elif dice1 > dice2:
    print("Dice #1 is larger")
else:
    print("Dice #2 is larger")

t.fillcolor("blue")
t.begin_fill()
for k in range(8):
    t.forward(100)
    t.left(45)

t.end_fill()
t.done()