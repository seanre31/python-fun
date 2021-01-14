import random


count = 0

while True:
    count +=1
    diceX = random.randint(1,7)
    diceY = random.randint(1,7)
    print("Dice X Rolled: ", diceX)
    print("Dice Y Rolled: ", diceY)
    print("-----")
    if diceX == diceY:
        break
    
print("There were", count, "rolls before a matching pair was rolled")
print("The matching pair was", diceX, "&",diceY)
