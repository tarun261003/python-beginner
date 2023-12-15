from tarun.print import print_slow
print_slow('Percentage calaculator:')
print_slow('Enter the number of subjects:')
num=int(input('>>'))
print_slow('Enter your total marks:')
marks=int(input('>>'))
per=(marks/(num*100))*100
print_slow('The percentage of your marks  is %.2f'%(per))