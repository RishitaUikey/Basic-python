'''Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
Sample Data:
("1981-1991") -> 2
("2000-2020") -> 6'''
def count_leap_years(year_range):

    start_year, end_year = map(int, year_range.split('-'))
    leap_year_count = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_year_count += 1
    
    return leap_year_count
samples = [
    "1981-1991",
    "2000-2020"
]
for sample in samples:
    print(f'("{sample}") -> {count_leap_years(sample)}')
