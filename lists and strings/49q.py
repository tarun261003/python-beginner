from tarun.print import print_slow

print_slow('Enter the elements of the list:')
l1=list(map(int,input(">>").split()))
d={}
for i in l1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print_slow('The frequrncy of the list items are:')
print(d)