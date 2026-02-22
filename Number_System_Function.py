# 1. Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci (nth term)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


# 4. Sum of digits
def sum_of_digits(n):
    total = 0
    for d in str(abs(n)):
        total += int(d)
    return total


# 5. Reverse number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num


# 6. Armstrong number check
def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == n


# 7. GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 8. LCM
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# 9. Perfect number check
def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


# 10. Menu-driven program
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 10:
                print("Exited successfully.")
                break

            elif choice == 1:
                n = int(input("Enter number: "))
                print("Factorial:", factorial(n))

            elif choice == 2:
                n = int(input("Enter number: "))
                print("Is Prime:", is_prime(n))

            elif choice == 3:
                n = int(input("Enter term number: "))
                print("Fibonacci:", fibonacci(n))

            elif choice == 4:
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == 5:
                n = int(input("Enter number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == 6:
                n = int(input("Enter number: "))
                print("Is Armstrong:", is_armstrong(n))

            elif choice == 7:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == 8:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == 9:
                n = int(input("Enter number: "))
                print("Is Perfect Number:", is_perfect_number(n))

            else:
                print("Invalid choice! Please select from the menu.")

        except ValueError:
            print("Invalid input! Please enter integers only.")


# Run the program
math_menu()