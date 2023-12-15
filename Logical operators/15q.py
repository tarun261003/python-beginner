def complex_logical_expression(a, b, c, d):
    """
    Evaluate a complex logical expression.

    Parameters:
    - a, b, c, d: Boolean values.

    Returns:
    - The result of the logical expression.
    """
    result = (a and b) or (c and not d)
    return result

# Example usage:
# Get input from the user (assuming the input is boolean values)
a = bool(input("Enter boolean value for 'a' (True/False): "))
b = bool(input("Enter boolean value for 'b' (True/False): "))
c = bool(input("Enter boolean value for 'c' (True/False): "))
d = bool(input("Enter boolean value for 'd' (True/False): "))

# Evaluate the complex logical expression
result = complex_logical_expression(a, b, c, d)

# Display the result
print(f"The result of the complex logical expression is: {result}")
