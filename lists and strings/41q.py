from tarun.print import print_slow

print_slow('Enter the list items with spaces:')
a=list(map(int,input('>>').split()))
print_slow(f'{a}')