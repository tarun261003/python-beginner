from tarun.print import print_slow
from math import sqrt
print_slow('Perfect square checker:')
print_slow('Enter the number:')
n=int(input('>>'))
s1=sqrt(n)
if s1.is_integer():
    print_slow('Pefect square')
else:
    print_slow('Not a perfect square')