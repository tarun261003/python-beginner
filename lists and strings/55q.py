from tarun.print import print_slow

print_slow('Enter the list to find the ascending order of the list:')
a=list(map(int,input('>>').split()))
print_slow(f'The ascending order of the list is \n{sorted(a)}')