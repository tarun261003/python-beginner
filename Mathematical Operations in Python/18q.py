from tarun.print import print_slow
print_slow('Sum of n numbers..')
print_slow('Enter the n value to get the sum:')
n=int(input('>>'))
sum=(n*(n+1))//2
print_slow(f'The sum of {n} natural numbers is {sum}')


'''
                or
sum1=0
for i in range(n+1):
    sum1+=i
print_slow(f'Loop sum is {sum1}')
'''