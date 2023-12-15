from tarun.print import print_slow
print_slow('Enter the number here:')
num=int(input('>>'))
sum=0
temp=num
while num!=0:
    rem=num%10
    sum+=rem
    num//=10
print_slow(f'The sum of digits in the number {temp} is {sum}')
'''             or
num=input('Enter the number:')
sum=0
for i in num:
    sum+=int(i)
print(sum)
'''