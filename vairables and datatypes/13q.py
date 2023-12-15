from tarun.print import print_slow

print_slow('Simple Interest Calaculator!')
print_slow('Enter the principal amount:')
p=float(input('>>'))
print_slow('Enter the time for the amount:')
t=int(input('>>'))
print_slow('Enter the rate of interrest')
r=float(input('>>'))
print_slow(f'The simple interest is {(p*t*r)/100}')