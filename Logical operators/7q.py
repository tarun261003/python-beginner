print('Enter a num:')
a=int(input('>>'))
odd=a%2!=0
pos=a>0
if odd and pos:
    print('ok')
else:
    print('no')