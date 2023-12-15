import time
def print_slow(text,delay=0.03):
    for char in text:
        print(char,end='')
        time.sleep(delay)
    print()
if __name__=="__main__":
    pass