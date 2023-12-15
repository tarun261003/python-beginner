from tarun.print import print_slow
from math import sqrt
print_slow('Hypotenuse calaculator..')
#formula -> h**2=s1**2+s2**2
print_slow('Enter side a:')
a=int(input('>>'))
print_slow('Enter side b:')
b=int(input('>>'))
hyp=sqrt(a**2+b**2)
print_slow(f'The hypotenuse with sides {a} and {b} is {int(hyp)}')
