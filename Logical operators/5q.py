from tarun.print import print_slow
def has_special(password):
    return any(chr for chr in password if chr.isascii() and not chr.isalnum())
def pass_cecker(password):
    l=any(chr for chr in password if chr.islower())
    u=any(chr for chr in password if chr.isupper())
    n=any(chr for chr in password if chr.isnumeric())
    le=True if len(password)>=8 else False
    if l and u and n and le:
        return True
    else:
        return False
print_slow('Enter password:')
p=input('>>')
print_slow(f'{"Fine" if pass_cecker(p) else "Recheck the password,requirements not satisfied"}')