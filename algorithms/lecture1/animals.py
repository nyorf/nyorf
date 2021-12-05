from algohelper import exectime
from time import sleep
from time import time as timer

def test():
    print("hello, world")
    sleep(5)

def main():
    return test()

if __name__ == '__main__':
    print(exectime(main()))