import random
print('Random password')
n=int(input('Enter the length of the string:'))
alpha='abcdefghijklmnopqrstuvwxyz'
small=list(alpha)
caps=list(alpha.upper())
num=list('1234567890')
spec=list('~!@#$%^&*()_')
combine=small+caps+num+spec
a=[]
a.extend(random.choice(caps))
a.extend(random.choice(small))
a.extend(random.choice(num))
a.extend(random.choice(spec))
random.shuffle(a)
psw=''.join(a)
for i in range(n-4):
    psw+=random.choice(combine)
print(len(psw))
print(psw)