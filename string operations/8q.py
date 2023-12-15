from tarun.print import print_slow
#Create a program that deletes characters from a string using slicing.	
a='Python programming'
print_slow(f'Enter index to remove the charecter:(0 to {len(a)-1})')
n=int(input('>>'))
try:
    a=a.replace(a[n],'')
except Exception as e:
    print(e)
    print_slow('No such index in the string..')
finally:
    print_slow(a)
