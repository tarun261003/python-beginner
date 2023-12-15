from tarun.print import print_slow

print_slow('Swapping..')
print_slow('Enter number 1:')
x=int(input('>>'))
print_slow('Enter number 2:')
y=int(input('>>'))
print_slow(f'The original values are {x} and {y}')
temp=x
x=y
y=temp
print_slow(f'The swapped values are {x} and {y}')