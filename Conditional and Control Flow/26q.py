from tarun.print import print_slow
print_slow('Maximum of three numbers:')
print_slow('Enter the three numbers.:')
a,b,c=map(int,input('>>').split())
if a>b:
    if a>c:
        max=a
    else:
        max=c
else:
    if b>c:
        max=b
    else:
        max=c
print_slow(f'The maximum number b/w the numbers {a},{b},{c} is {max}')