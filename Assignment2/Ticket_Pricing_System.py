# Taking inputs
age = int(input("Enter age: "))
day = input("Enter day of the week: ").lower()
number_of_tickets = int(input("Enter number of tickets: "))

# Determining base price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif age >= 3 and age <= 12:
    base_price = 150
    category = "Child"
elif age >= 13 and age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Calculating total base amount
total_base_price = base_price * number_of_tickets

# Determining discount
if day in ["friday", "saturday", "sunday"]:
    discount_percentage = 20
    discount_amount = (discount_percentage / 100) * total_base_price
else:
    discount_percentage = 0
    discount_amount = 0

# Final amount after discount
final_amount = total_base_price - discount_amount

# Displaying results
print("\n=== TICKET PRICE DETAILS ===")
print("Age Category:", category)
print("Base price per ticket: ₹", base_price)
print("Number of tickets:", number_of_tickets)
print("Total base price: ₹", total_base_price)
print("Discount:", discount_percentage, "%")
print("Discount amount: ₹", discount_amount)
print("Price after discount: ₹", final_amount)