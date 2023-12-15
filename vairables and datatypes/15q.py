from tarun.print import print_slow
print_slow('Numerical system')
print_slow('Enter thr number to check whether +ve,-ve or 0:')
n1=int(input('>>'))
if(n1==0):
    print_slow('The number is 0')
elif(n1>0):
    print_slow(f'The Number {n1} is  positive')
else:
    print_slow(f'The number {n1} is negative')