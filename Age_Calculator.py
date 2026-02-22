# Taking input from the user
birth_year = int(input("Enter your birth year: "))
current_year = 2026   # You can update this if needed

# Calculating age
age_years = current_year - birth_year
age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Displaying results
print("\nAge Details:")
print("Current age (years):", age_years)
print("Age in months:", age_months)
print("Age in days:", age_days)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)
print("Years until age 100:", years_to_100)