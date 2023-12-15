from tarun.print import print_slow
def swap(str1):
    temp=""
    for i in a:
        if i.islower():
            temp+=i.upper()
        elif i.isupper():
            temp+=i.lower()
        else:
            temp+=i
    return temp
if __name__=="__main__":
    print_slow('Enter the string:')
    a=input('>>')
    a=swap(a)
    print_slow('The swapped string is :')
    print_slow(a)