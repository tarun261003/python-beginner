from tarun.print import print_slow
print_slow('Enter the string:')
a=input('>>')
print_slow('Enter the substring:')
sub=input('>>')
if sub in a:
    print_slow('Substring is in a')
else:
    print_slow('Substring is not in a')