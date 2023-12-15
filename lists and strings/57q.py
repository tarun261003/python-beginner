from tarun.print import print_slow

print_slow('Enter a word to extract vowels from the word:')
l1=[]
vowels=list('aeiou')
inp=input('>>').lower()
for i in inp:
    if i in vowels:
        l1.append(i)
print(f"The vowels in the word {inp} is {l1}")