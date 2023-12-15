from tarun.print import print_slow
print_slow('Enter the two lists:')
a=input('>>').split()
b=input('>>').split()
common=[]
for i in a:
    if i in b and i not in common:
        common.append(i)
print_slow(f'The common elements of the both lists is {common}')