def is_eligible_for_discount(age, has_disability):
    """
    Determine if a person is eligible for a discounted bus fare.

    Parameters:
    - age: Age of the person.
    - has_disability: True if the person has a disability, False otherwise.

    Returns:
    - True if eligible for a discount, False otherwise.
    """
    # Define eligibility criteria
    age_limit_for_discount = 12  # Children and seniors may be eligible for a discount
    has_disability_discount = has_disability

    # Check eligibility using logical operators
    is_eligible = (age <= age_limit_for_discount) or has_disability_discount

    return is_eligible

# Example usage:
# Get input from the user
age = int(input("Enter your age: "))
has_disability = input("Do you have a disability? (yes/no): ").lower() == 'yes'

# Check if the person is eligible for a discounted bus fare
eligible_for_discount = is_eligible_for_discount(age, has_disability)

# Display the result
if eligible_for_discount:
    print("You are eligible for a discounted bus fare.")
else:
    print("You are not eligible for a discounted bus fare.")
