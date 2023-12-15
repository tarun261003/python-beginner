from tarun.print import print_slow

print_slow('Enter a statemt to captilize each word:')
sen=input('>>')
words=sen.split()
temp=[i.capitalize() for i in words]
print_slow('The capitalized sentense is as follows:')
print_slow(f'{" ".join(temp)}')