def is_vowel_or_digit(char):
    """
    Check if a given character is a vowel or a digit.

    Parameters:
    - char: The character to be checked.

    Returns:
    - True if the character is a vowel or a digit, False otherwise.
    """
    # Define the vowels
    vowels = "aeiouAEIOU"

    # Use logical operators to check if the character is a vowel or a digit
    is_vowel = char in vowels
    is_digit = char.isdigit()

    return is_vowel or is_digit

# Example usage:
# Get input from the user
character = input("Enter a character: ")

# Check if the character is a vowel or a digit
result = is_vowel_or_digit(character)

# Display the result
if result:
    print(f"{character} is a vowel or a digit.")
else:
    print(f"{character} is neither a vowel nor a digit.")
