#take user input
n = int(input("How many numbers? "))

numbers = []

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / n
maximum = max(numbers)
minimum = min(numbers)

numbers.sort()

if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_count = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_count]

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Median:", median)
print("Mode:", modes)