from tarun.print import print_slow
print_slow('Fibonacci series')
a=0
b=1
n=15
print(f'1->{a}')
print(f'2->{b}')
count=3
for i in range(0,n-2):
    c=a+b
    print(f'{count}->{c}')
    a=b
    b=c
    count+=1