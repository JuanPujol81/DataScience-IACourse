def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        operator = input("Enter the operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operator! Please enter a valid operator.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return

    print("Result:", result)