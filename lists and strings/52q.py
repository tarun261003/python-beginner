from tarun.print import print_slow

print_slow('Enter the list to find the average of the numbers in the list:')
la=list(map(int,input('>>').split()))
sum=0
for i in la:
    sum+=i
print_slow(f'The average of numbers in the list {la} is {sum/len(la)}')