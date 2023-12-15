from tarun.print import print_slow
print_slow('Modules of the number:')
print_slow('Enter the number to check whether it is even or odd')
a=int(input('>>'))
print_slow(f'The remainder is {a%2}')
temp="Even" if a%2==0 else "Odd"
print_slow(f'The number is {temp}')