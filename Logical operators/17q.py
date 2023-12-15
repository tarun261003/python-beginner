def is_valid_email(email):
    """
    Check if a given string is a valid email address.

    Parameters:
    - email: The string to be checked.

    Returns:
    - True if the email is valid, False otherwise.
    """
    # Check for the presence of '@' and '.'
    if '@' in email and '.' in email:
        # Check if '@' appears before '.'
        if email.index('@') < email.index('.'):
            # Check if there is at least one character before '@' and after '.'
            if email.index('@') > 0 and email.index('.') < len(email) - 1:
                return True

    return False

# Example usage:
email_input = input("Enter an email address: ")
result = is_valid_email(email_input)

# Display the result
if result:
    print("The entered email address is valid.")
else:
    print("The entered email address is not valid.")
