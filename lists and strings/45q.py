from tarun.print import print_slow

print_slow('Enter a word to check whether it is palindrome or not:')
inp=input('>>').lower()
if inp==inp[::-1]:
    print_slow(f'The word "{inp}" is a palindrome.')
else:
    print_slow(f'The word "{inp}" is not a palindrome.')