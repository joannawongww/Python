number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = (input("Choose addition or subtraction: "))

if operator == "addition":
    print(number1 + number2)

elif operator == "subtraction":
    print(number1 - number2)

else:
    print("Unknown operator")
