operNum = int(input('How many operations would you like to perform: ')) 

for x in range(int(operNum)):
    num1 = int(input('Please enter a number: ')) 
    num2 = int(input('Please enter a number: ')) 
    print("1. Add")
    print("2. Subract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    operType = int(input('Which operation would you like to perform: ')) 
    
    def add():
        result = num1 + num2
        print("The result is", result)
    def subract():
        result = num1 - num2
        print("The result is", result)
    def multiply():
        result = num1 * num2
        print("The result is", result)
    def divide():
        result = num1 / num2
        print("The result is", result)
    def remainder():
        result = num1 % num2
        print("The result is", result)
    if operType == 1:
        add()
    if operType == 2:
        subract()
    if operType == 3:
        multiply()
    if operType == 4:
        divide()
    if operType == 5:
        remainder()

