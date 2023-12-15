from tarun.print import print_slow
print_slow('Even or odd checker..')
print_slow('Enter a number:')
n=int(input('>>'))
temp="Even" if n%2==0 else "Odd"
print_slow(f'The number {n} is {temp}')