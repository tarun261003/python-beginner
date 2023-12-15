import math

def is_equilateral_and_obtuse_triangle(side1, side2, side3, angle1, angle2, angle3):
    """
    Check if a triangle is equilateral and has an angle greater than 90 degrees.

    Parameters:
    - side1, side2, side3: Lengths of the sides of the triangle.
    - angle1, angle2, angle3: Measures of the angles in degrees.

    Returns:
    - True if the triangle is equilateral and has an angle greater than 90 degrees, False otherwise.
    """
    # Check if the triangle is equilateral
    is_equilateral = side1 == side2 == side3

    # Check if the triangle has an angle greater than 90 degrees
    is_obtuse = any(angle > 90 for angle in (angle1, angle2, angle3))

    # Return True if both conditions are met
    return is_equilateral and is_obtuse

# Example usage:
side_length = 5
angle_measure = 100

# For an equilateral triangle with an angle greater than 90 degrees
result = is_equilateral_and_obtuse_triangle(side_length, side_length, side_length, angle_measure, angle_measure, angle_measure)

# Display the result
if result:
    print("The triangle is equilateral and has an angle greater than 90 degrees.")
else:
    print("The triangle does not meet the specified conditions.")
