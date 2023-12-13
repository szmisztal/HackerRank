import calendar

def is_leap(year):
    leap = False
    if calendar.isleap(year):
        leap = True
    return leap

print(is_leap(2024))
