from tarun.print import print_slow

print_slow('Enter the elements of the list:')
l1=list(map(int,input(">>").split()))
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print_slow(f'The unique elements of the list is :{l2}')