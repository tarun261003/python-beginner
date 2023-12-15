def is_valid_date(year, month, day):
    """
    Check if a date is in a valid range.

    Parameters:
    - year: Year of the date.
    - month: Month of the date.
    - day: Day of the date.

    Returns:
    - True if the date is in a valid range, False otherwise.
    """
    # Define the valid date range
    min_year, max_year = 1900, 2100
    min_month, max_month = 1, 12
    min_day, max_day = 1, 31

    # Check if the date is within the valid range
    is_valid = (
        min_year <= year <= max_year and
        min_month <= month <= max_month and
        min_day <= day <= max_day
    )

    return is_valid

# Get input from the user
year = int(input("Enter the year (yyyy): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

# Check if the date is valid
if is_valid_date(year, month, day):
    print("The entered date is in a valid range.")
else:
    print("The entered date is not in a valid range.")
