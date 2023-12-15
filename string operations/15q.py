from tarun.print import print_slow

print_slow('Enter the string to find the frequency:')
str1=input('>>')
print_slow('Enter the charecter:')
chr=input('>>')
d={}
for i in str1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print_slow(f"The charecter '{chr} is occured {d[chr]} times'")