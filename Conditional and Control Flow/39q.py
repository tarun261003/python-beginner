from tarun.print import print_slow

print_slow('Palindrome check:')
print_slow('Enter the string:')
a=input('>>')
r_a=a[::-1]
temp="a Palindrome" if a==r_a else "not a Palindrome"
print_slow(f'The string "{a}" is {temp}')