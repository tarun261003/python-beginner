from tarun.print import print_slow
def leap_year(yr):
    leap=False
    if yr%4==0:
        leap=True
        if yr%100==0:
            leap=False
            if yr%400==0:
                leap=True
    else:
        leap=False
    return leap
print_slow('Leap year checker..')
print_slow('Enter the year:')
yr=int(input('>>'))
temp="a Leap Year" if leap_year(yr) else "Not a Leap year"
print_slow(f'The year {yr} is {temp}')