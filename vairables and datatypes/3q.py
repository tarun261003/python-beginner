import time
def print_slow(text,delay=0.03):
    for char in text:
        print(char,end='')
        time.sleep(delay)
    print()
print_slow('AREA OF RECTANGLE:')
print_slow('Enter the length of rectangle:')
length=int(input('>>'))
print_slow('Enter the width of rectangle:')
breadth=int(input('>>'))
area=length*breadth
print_slow(f'The area is {area}')