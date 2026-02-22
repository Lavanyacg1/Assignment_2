number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

results = []

print(f"\nMultiplication Table of {number}")
for i in range(1, end + 1):
    value = number * i
    results.append(value)
    print(f"{number} x {i} = {value}")

