from tarun.print import print_slow

print_slow('Sum of 100 natural numbers.')
sum=0
for i in range(1,101):
    sum+=i
print_slow(f'The sum of 100 natural numbers is {sum}')