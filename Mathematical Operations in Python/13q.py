from tarun.print import print_slow
from math import log
print_slow('Logirithm of a number:')
print_slow('Enter the number:')
a=input('>>').lower()
if a=='e':
    print_slow('The logirithm of number {a} is 1')
else:
    print_slow(f'The logirithm of number {a} is {log(int(a))}')