from tarun.print import print_slow

print_slow("Enter a word to check whether to check it contains 'e' or not")
a=input('>>').lower()
if 'e' in a:
    print_slow("It contains 'e'")
else:
    print_slow("It doesn't contain 'e'")