from tarun.print import print_slow

print_slow('Enter the string:')
inp=input('>>')
len1=0
for i in inp:
    len1+=1
print_slow(f'The length of the string is {len1}')