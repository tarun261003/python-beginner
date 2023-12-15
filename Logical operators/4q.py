from tarun.print import print_slow

print_slow('Enter your age:')
try:
    age=int(input('>>'))
except Exception as e:
    print_slow('Enter valid age..')
    age=int(input('>>'))
if age>=18:
    print_slow('Apply for voter id elections are in march,2024')
else:
    print_slow(f'You have {18-age} years to apply')