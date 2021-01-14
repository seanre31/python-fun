width = int(input("Please enter a width for your grid:"))

rows = int(input("Please enter the amount of rows in your grid:"))

for x in range(rows):
    for y in range(width):
        print('*',end = ' ')
    print()
