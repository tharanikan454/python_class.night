def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = 2024
result = is_leap_year(year)
print(f"Is {year} a leap year? {result}")
