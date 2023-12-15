from tarun.print import print_slow
print_slow('The text you input here will be updated in the file.')
a=input('>>')
with open('check.txt','w') as f:
    print(a,file=f)
thumbs_up_emoji = "\U0001F44D"
print('Updated,done',thumbs_up_emoji)