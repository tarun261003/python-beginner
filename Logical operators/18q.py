def is_prime_and_greater_than_10(number):
    """
    Check if a number is a prime number and greater than 10.

    Parameters:
    - number: The number to be checked.

    Returns:
    - True if the number is prime and greater than 10, False otherwise.
    """
    # Check if the number is greater than 10
    if number <= 10:
        return False

    # Check if the number is a prime number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage:
# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime and greater than 10
result = is_prime_and_greater_than_10(num)

# Display the result
if result:
    print(f"{num} is a prime number and greater than 10.")
else:
    print(f"{num} is not a prime number or not greater than 10.")
