def is_palindrome_recursively(word):
    # Base case: if the word has 0 or 1 character, it's a palindrome
    if len(word) <= 1:
        return True
    # Compare the first and last characters (case insensitive)
    if word[0] != word[-1]:
        return False
    # Recur on the substring that excludes the first and last characters
    return is_palindrome_recursively(word[1:-1])

def is_palindrome_with_loop(word):
    # Loop to check if the word is a palindrome
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    print("\U0001f31fPalindrome Checker\U0001f31f")
    while True:
        word = input("Input a word (or type 'exit' to quit) > ").strip().lower()  # Standardize the input
        if word == 'exit':
            print("Goodbye!")
            break

        # Recursive check
        if is_palindrome_recursively(word):
            print(f"{word.capitalize()} is a palindrome. Yay!")
        else:
            print(f"{word.capitalize()} is not a palindrome.")

if __name__ == "__main__":
    main()
