from tarun.print import print_slow
def is_leap(yr):
    four=yr%4==0
    hun=yr%100==0
    fh=yr%400==0
    result=four and (not hun or fh)
    return result
print_slow('Enter the year:')
yr=int(input('>>'))
print_slow(f'{"Leap year" if is_leap(yr) else "Not a leap year"}')