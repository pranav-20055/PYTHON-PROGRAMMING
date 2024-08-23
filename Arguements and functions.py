def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def next_leap_year(current_year):
    next_year = current_year + 1
    while not is_leap_year(next_year):
        next_year += 1
    return next_year

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

next_leap = next_leap_year(year)
print(f"The next leap year after {year} is {next_leap}.")
