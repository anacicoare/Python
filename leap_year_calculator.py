year = int(input("Which year would you like to check?\n"))
if year % 4 == 0:
    div_4 = 1
else:
    div_4 = 0

if year % 100 == 0:
    div_100 = 1
else:
    div_100 = 0

if year % 400 == 0:
    div_400 = 1
else:
    div_400 = 0

is_leap = 0

if div_4 == 1:
    if div_100 == 1:
        if div_400 == 1:
            print(f"{year} is a leap year.")
            is_leap = 1

if is_leap == 0:
    print(f"{year} is not a leap year.")
