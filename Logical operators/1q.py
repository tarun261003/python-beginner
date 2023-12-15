from tarun.print import print_slow
print_slow('Enter a range:')
r=int(input('>>'))
for i in range(1,r):
    if i%2==0 and i%3==0:
        print_slow(f'{i}')