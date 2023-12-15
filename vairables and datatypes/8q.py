from tarun.print import print_slow

print_slow('Enter the number :')
x=int(input('>>'))
if x%5==0 and x%7==0:
    print_slow(f'The number {x} is divisible by the both numbers')