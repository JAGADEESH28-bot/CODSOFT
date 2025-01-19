def calculator():
    print("Welcome to the Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.")

    while True:
        operation = input("\nEnter operation: ").lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2

            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
