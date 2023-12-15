from tarun.print import print_slow

print_slow('Length of list finder:')

print_slow('Enter the list items with spaces:')
l1=list(input('>>').split())
print_slow(f'The length of list {l1} is {len(l1)}')