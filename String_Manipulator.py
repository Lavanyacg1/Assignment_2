#Taking input from the user

sentence=input("Enter a sentence: ")

# Original sentence
print("Original:", sentence)

# Total characters (with spaces)
print("Characters (with spaces):", len(sentence))

# Total characters (without spaces)
print("Characters (without spaces):", len(sentence.replace(" ", "")))

# Total words
words = sentence.split()
print("Words:", len(words))

# Uppercase
print("UPPERCASE:", sentence.upper())

# Lowercase
print("lowercase:", sentence.lower())

# Title Case
print("Title Case:", sentence.title())

# First word
print("First word:", words[0])

# Last word
print("Last word:", words[-1])

# Reversed sentence
print("Reversed:", sentence[::-1])