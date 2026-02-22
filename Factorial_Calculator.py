#defining a function
def factorial_calculator(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    elif n == 0:
        return "0! = 1"

    else:
        factorial = 1
        steps = []

        for i in range(n, 0, -1):
            factorial *= i
            steps.append(str(i))

        return f"{n}! = " + " * ".join(steps) + f" = {factorial}"


# Main program
try:
    num = int(input("Enter a number: "))
    result = factorial_calculator(num)
    print(result)

except ValueError:
    print("Invalid input! Please enter an integer.")