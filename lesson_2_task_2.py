def is_year_leap(year):
    if year % 4 ==0:
        return True
    else:
        return False
year_to_year = 2026
result = is_year_leap(year_to_year)
print("год", year_to_year, ":", result)