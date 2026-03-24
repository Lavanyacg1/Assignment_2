# Taking input from the user
year = int(input("Enter a year: "))

# Checking leap year conditions
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("\nYear:", year)
    print("Result: Leap Year")
    print("Reason: Divisible by 4 and not divisible by 100, or divisible by 400.")
else:
    print("\nYear:", year)
    print("Result: NOT a Leap Year")
    print("Reason: Does not satisfy leap year rules.")