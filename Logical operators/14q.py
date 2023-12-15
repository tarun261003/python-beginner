def has_positive_and_negative_numbers(numbers):
    """
    Check if a list contains both positive and negative numbers.

    Parameters:
    - numbers: List of numbers.

    Returns:
    - True if the list contains both positive and negative numbers, False otherwise.
    """
    has_positive = any(num > 0 for num in numbers)
    has_negative = any(num < 0 for num in numbers)

    # Check if both conditions are met
    return has_positive and has_negative

# Example usage:
numbers_list1 = [1, -2, 3, -4, 5]
numbers_list2 = [1, 2, 3, 4, 5]

# Check if each list contains both positive and negative numbers
result1 = has_positive_and_negative_numbers(numbers_list1)
result2 = has_positive_and_negative_numbers(numbers_list2)

# Display the results
print(f"List 1: {result1}")
print(f"List 2: {result2}")
