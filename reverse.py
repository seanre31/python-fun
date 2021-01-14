num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a number: '))
num3 = int(input('Please enter a number: '))
num4 = int(input('Please enter a number: '))
num5 = int(input('Please enter a number: '))

numList = [num1, num2, num3, num4, num5]

i = len(numList) - 1

while i >= 0 :
    print(numList[i]) 
    i -= 1
