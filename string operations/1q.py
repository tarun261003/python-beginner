from tarun.print import print_slow
print_slow('Enter the string to slice:')
a1=input('>>')
print_slow('Enter the start index:')
l=int(input('>>'))
print_slow('Enter the last index:(excluding the element at that index)')
h=int(input('>>'))
print_slow(f'The substring is {a1[l:h]}')