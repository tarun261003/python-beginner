from tarun.print import print_slow
print_slow('Multiplication table of given number:')
print_slow('Enter the number:')
n=int(input('>>'))
for i in range(1,11):
    print_slow(f'{n}x{i}={n*i}')