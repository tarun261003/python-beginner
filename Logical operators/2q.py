from tarun.print import print_slow
print_slow('Enter maths marks and sceince marks with space:')
m,s=map(int,input('>>').split())
if m>=40 and s>=40:
    print_slow('Passed in maths and science')
elif m>=40 and s<40:
    print_slow('Science is gone')
elif m<40 and s>=40:
    print_slow('maths gone')
else:
    print_slow('Both subs are failed')