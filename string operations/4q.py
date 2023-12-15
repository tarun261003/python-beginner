from tarun.print import print_slow

print_slow('Modifying elements by index:')
print_slow('Enter the string:')
a=input('>>')
print_slow('Enter the index to access the element:')
n=int(input('>>'))
key=input('Enter the charecter value')
try:
    a=a.replace(a[n],key)
    print_slow(f"The word  is {a}")
except Exception as e:
    print(e)