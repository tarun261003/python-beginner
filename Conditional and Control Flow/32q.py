from tarun.print import print_slow

print_slow('Vowel or consonant checker.')
vowels=tuple('aeiou')
print_slow('Enter charecter:')
ch=input('>>').lower()
if ch in vowels:
    print_slow('Vowel')
else:
    print_slow('Consonant')