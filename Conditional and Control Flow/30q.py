from tarun.print import print_slow

print_slow('Prime NUmber checker..')
print_slow('Enter the number :')
n=int(input('>>'))
c=0
for i in  range(2,n//2+1):
    if n%i==0:
        c+=1
        break
if c==0:
    print_slow(f'The number {n} is a prime number')
else:
    print_slow(f'The number {n} is not a prime number')