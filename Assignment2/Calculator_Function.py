# calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

# Advanced calculator functions (no import)
def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of negative number"
    return a ** 0.5

def percentage(a, b):
    return (a / 100) * b


# Main calculator function
def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 9:
                print("Calculator closed. Thank you!")
                break

            elif choice == 7:
                a = float(input("Enter number: "))
                print("Result:", square_root(a))

            elif choice == 8:
                a = float(input("Enter percentage value: "))
                b = float(input("Enter total value: "))
                print("Result:", percentage(a, b))

            elif 1 <= choice <= 6:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    print("Result:", add(a, b))
                elif choice == 2:
                    print("Result:", subtract(a, b))
                elif choice == 3:
                    print("Result:", multiply(a, b))
                elif choice == 4:
                    print("Result:", divide(a, b))
                elif choice == 5:
                    print("Result:", modulus(a, b))
                elif choice == 6:
                    print("Result:", power(a, b))

            else:
                print("Invalid choice! Please select from menu.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Run the calculator
calculator()