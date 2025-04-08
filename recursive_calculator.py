# Define basic math operation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2  # Note: consider adding error handling for division by zero


# Dictionary to map operation symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print("Welcome to Python Calculator!")


def calculator():
    # Get the first number for the new calculation
    actively_calculating = True
    first_number = float(input("What's the first number?: "))

    # Inner loop: keep calculating with the current result
    while actively_calculating:
        # Display available operations
        for keys, value in operations.items():
            print(keys)

        # Get the operation and next number from the user
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        # Perform the selected operation
        result = operations[operation](first_number, second_number)

        # Show the result of the operation
        print(f"{first_number} {operation} {second_number} = {result}")

        # Ask if user wants to continue with the current result
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            first_number = result  # Update the starting number for next round
        else:
            actively_calculating = False  # Exit inner loop and start fresh
            print("\n" * 20)
            calculator()


calculator()
