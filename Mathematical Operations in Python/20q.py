from tarun.print import print_slow
print_slow('Average of three numbers..')
print_slow('Enter the three numbers with spaces..')
n1,n2,n3=tuple(map(int,input('>>').split()))
print_slow(f'''The average of the numbers {n1},{n2} and {n3} is {(n1+n2+n3)/3}     ''')