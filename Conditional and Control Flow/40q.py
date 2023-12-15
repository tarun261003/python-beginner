from tarun.print import print_slow
print_slow('Sum of digits in a number:')
print_slow('Enter the number:')
n=int(input('>>'))
sum=0
temp=n
while n!=0:
    sum+=(n%10)
    n//=10
print_slow(f'The sum of digits in {temp} is {sum}')