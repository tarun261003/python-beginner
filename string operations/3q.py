from tarun.print import print_slow
print_slow('Accesing elements by index:')
print_slow('Enter the string:')
a=input('>>')
print_slow('Enter the index to access the element:')
n=int(input('>>'))
try:
    print_slow(f"The charecter at {n} is {a[n]}")
except Exception as e:
    print_slow('Index not Found')