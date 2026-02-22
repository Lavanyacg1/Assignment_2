#Taking input from thr user
first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))

#performing calculations
addition=first_number+second_number
subtraction=first_number-second_number
multiplication=first_number*second_number
division=first_number/second_number
modulus=first_number%second_number
exponentiation=first_number**second_number

#Displaying Results
print("Results:")
print(first_number,"+",second_number,"=",addition)
print(first_number,"+",second_number,"=",subtraction)
print(first_number, "*", second_number, "=", multiplication)
print(first_number, "/", second_number, "=", round(division, 2))
print(first_number, "%", second_number, "=", modulus)
print(first_number, "^", second_number, "=", exponentiation)
