"""
Program Name: Grade Calculator
Description : Calculates total, percentage, grade and result
Author      : Lavanya C G
"""

# Taking marks input
Kannada = int(input("Enter marks for kannada: "))
English = int(input("Enter marks for english: "))
Hindi = int(input("Enter marks for hindi: "))
Social = int(input("Enter marks for social: "))
Science = int(input("Enter marks for acience: "))

# Displaying marks
print("\nMarks in each subject:")
print("Kannada:", Kannada)
print("English:", English)
print("Hindi:", Hindi)
print("Social:", Social)
print("Science:", Science)

# Calculating total and percentage
total_marks = Kannada + English + Hindi+ Social + Science
percentage = (total_marks / 500) * 100

# Determining result
if Kannada >= 40 and English>= 40 and Hindi >= 40 and Social >= 40 and Science >= 40:
    result = "Pass"
else:
    result = "Fail"

# Determining grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Displaying results
print("\nTotal Marks:", total_marks, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)