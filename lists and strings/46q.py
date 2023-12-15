from tarun.print import print_slow

print_slow('Enter the elements of the list')
l1=list(map(int,input('>>').split()))
print_slow(f'The Maximum element of the list is {max(l1)}')