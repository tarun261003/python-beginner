from tarun.print import print_slow

print_slow('append() method is used to add element at end of the list')
a=[1,2,3,'dish',('a',2,3,4.0)]
print_slow('''Enter a number:\n1.int\n2.float\n3.str\n''')
choice=int(input('>>'))
print_slow('Enter an element to add:')
if choice==1:
    a.append(int(input('>>')))
    print_slow(f'{a}')
elif choice==2:
    a.append(float(input('>>')))
    print_slow(f'{a}')
else:
    a.append(input('>>'))
    print_slow(f'{a}')