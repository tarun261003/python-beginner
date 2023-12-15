def check_eligibility(age, is_member):
    """
    Determine if a person is eligible for a senior discount.

    Parameters:
    - age: Age of the person.
    - is_member: True if the person is a member, False otherwise.

    Returns:
    - True if eligible, False otherwise.
    """
    senior_age = 65
    senior_discount_eligible = age >= senior_age or is_member
    return senior_discount_eligible

# Example usage:
# Get input from the user
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == 'yes'

# Check eligibility
eligible_for_discount = check_eligibility(age, is_member)

# Display the result
if eligible_for_discount:
    print("Congratulations! You are eligible for a senior discount.")
else:
    print("Sorry, you are not eligible for a senior discount.")
