from tarun.print import print_slow
def leap_year(x):
    leap=False
    if x%4==0:
        leap=True
        if x%400==0:
            leap=False
        if x%100==0:
            leap=True
    else:
        leap=False
    return leap
print_slow('Leap year Checker:')
print_slow('Enter the year:')
x=int(input('>>'))
temp="Leap year" if leap_year(x) else "Not a leap year"
print_slow(f'The year {x} is {temp}')