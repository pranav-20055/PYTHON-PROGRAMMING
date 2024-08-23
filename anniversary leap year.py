# Input: Anniversary date in the format DD/MM/YYYY
date_input = input("Enter Date (DD/MM/YYYY): ")

# Extract day, month, and year from input
day, month, year = map(int, date_input.split('/'))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Given Anniversary Year: Leap Year.")
    # Print the next anniversary year
    next_anniversary_year = year + 1
    print(f"Anniversary Date: {day:02}/{month:02}/{next_anniversary_year}")
else:
    print(f"Given Anniversary Year: Non Leap Year.")
    # Print the previous anniversary year
    previous_anniversary_year = year - 1
    print(f"Anniversary Date: {day:02}/{month:02}/{previous_anniversary_year}")
