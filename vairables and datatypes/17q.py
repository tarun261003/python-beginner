from tarun.print import print_slow

print_slow('Decimal to Binary conversion:')
print_slow('Enter the number:')
num=int(input('>>'))
print_slow(f'The Binary number of {num} is {bin(num).lstrip("0b")}')