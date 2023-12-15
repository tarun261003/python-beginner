def is_valid_username(username):
    """
    Check if the username is valid.

    Parameters:
    - username: The username to be checked.

    Returns:
    - True if the username is valid, False otherwise.
    """
    # Validate username criteria (e.g., length, no spaces)
    return len(username) >= 5 and ' ' not in username

def is_valid_password(password):
    """
    Check if the password is valid.

    Parameters:
    - password: The password to be checked.

    Returns:
    - True if the password is valid, False otherwise.
    """
    # Validate password criteria (e.g., length, at least one digit)
    return len(password) >= 8 and any(char.isdigit() for char in password)

# Example usage:
# Get input from the user
username_input = input("Enter a username: ")
password_input = input("Enter a password: ")

# Validate the username and password
is_valid_username_input = is_valid_username(username_input)
is_valid_password_input = is_valid_password(password_input)

# Display the validation results
if is_valid_username_input and is_valid_password_input:
    print("Username and password are valid.")
elif not is_valid_username_input:
    print("Invalid username. Please make sure it has at least 5 characters and no spaces.")
else:
    print("Invalid password. Please make sure it has at least 8 characters and contains at least one digit.")
