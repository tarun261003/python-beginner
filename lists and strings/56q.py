from tarun.print import print_slow

print_slow('Enter the list items to find the occurence of the element in the list:')
a=input('>>').split()
print_slow('Enter the key element:')
key=input('>>')
print_slow(f'The first occurence of {key} is {a.index(key)}')