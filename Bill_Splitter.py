total_bill = float(input("Enter total bill: "))
number_of_people = int(input("Number of people: "))
tax_percentage = float(input("Tax percentage: "))
tip_percentage = float(input("Tip percentage: "))

tax_amount = (tax_percentage / 100) * total_bill
bill_after_tax = total_bill + tax_amount
tip_amount = (tip_percentage / 100) * bill_after_tax
total_amount = bill_after_tax + tip_amount
per_person = total_amount / number_of_people

print("\n=== BILL BREAKDOWN ===")
print("Subtotal:    ₹{:.2f}".format(total_bill))
print("Tax ({}%):   ₹{:.2f}".format(tax_percentage, tax_amount))
print("After tax:   ₹{:.2f}".format(bill_after_tax))
print("Tip ({}%):   ₹{:.2f}".format(tip_percentage, tip_amount))
print("Total:       ₹{:.2f}".format(total_amount))
print("Per person:  ₹{:.2f}".format(per_person))