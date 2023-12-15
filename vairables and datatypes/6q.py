from tarun.print import print_slow

print_slow('Fahrenheit temperature to Celsius')
print_slow(f'The formula is c=(f-32)*(5/9)')
print_slow('Enter the farenhit value :')
f=float(input('>>'))
print_slow(f'The celcius value is {(f-32)*(5/9)}')