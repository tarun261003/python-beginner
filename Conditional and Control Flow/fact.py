from tarun.print import print_slow
print_slow('Factorial of a given number:')
print_slow('Enter the number:')
n=int(input('>>'))
fact=1
for i in range(1,n+1):
    fact*=i
print_slow(f'The factorial of {n} is {fact}')