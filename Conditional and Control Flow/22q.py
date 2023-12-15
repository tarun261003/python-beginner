from tarun.print import print_slow

print_slow('The even numbers b/w 1 and 20 is :')
for i in range(2,21):
    if i%2==0:
        print(i)
