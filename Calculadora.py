while True:
    num1 = input('Enter first number: ')
    num2 = input("Enter second number: ")
    opr = input("Choose an operator: 1 = Sum; 2 = Subtraction; 3 = Multiply; 4 = Division; 5 = Exit: ")
    if opr == "1":
        print(int(num1)+int(num2))
    elif opr == "2":
        print(int(num1)-int(num2))
    elif opr == "3":
        print(int(num1)*int(num2))
    elif opr == "4"and opr != "0":
        print(float(num1)/float(num2))
    elif opr !="5":
        print("Invalid Operation.")
    if opr == "5":
        break