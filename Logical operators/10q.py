a=input('Enter the string:')
result=any(chr for chr in a if chr.islower())
result1=any(chr for chr in a if chr.isupper())
print(f'{"The condition is satisfied" if result and result1 else "Condition is not satisfied"}')