
num1 = int(input('Please enter a number: ')) 
num2 = int(input('Please enter a number: ')) 
   
numList = [num1, num2]

def swap():
    print("You entered:", *numList, sep=" ")
    numListSwap = numList[::-1]
    print("Your numbers swapped:", *numListSwap, sep=" ")

swap()
