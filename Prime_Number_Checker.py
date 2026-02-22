# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Part 1: Check single number
try:
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

except ValueError:
    print("Invalid input! Please enter an integer.")


#Part 2: Prime numbers in a range
try:
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    primes = []

    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(str(i))

    if primes:
        print("Prime numbers:", ", ".join(primes))
    else:
        print("No prime numbers found in this range.")

except ValueError:
    print("Invalid input! Please enter integers only.")