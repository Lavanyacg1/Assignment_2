# define a function called palindrome_checker
def palindrome_checker(value):
    original = str(value)
    reversed_value = original[::-1]

    print(f"Original: {original}")
    print(f"Reversed: {reversed_value}")

    # Compare ignoring case
    if original.lower() == reversed_value.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT a palindrome")


# Main program
user_input = input("Enter word/number: ")
palindrome_checker(user_input)