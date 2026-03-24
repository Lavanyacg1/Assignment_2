# 1. Count words
def count_words(text):
    return len(text.split())


# 2. Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)


# 3. Count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch.isalpha() and ch not in vowels)


# 4. Reverse text
def reverse_text(text):
    return text[::-1]


# 5. Check palindrome (ignore spaces & case)
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


# 6. Remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in text if ch not in vowels)


# 7. Word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


# 8. Longest word
def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest, len(longest)


# 9. Analyze text
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    lw, length = longest_word(text)
    print(f"Longest word: {lw} ({length} letters)")

    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    print(", ".join(f"{k}: {v}" for k, v in freq.items()))


# Main program
text = input("Enter text: ")
analyze_text(text)