from time import time

def exectime(function):
    start = time()
    function
    end = time()
    result = end-start
    return result

if __name__ == '__main__':
    print('import this file via "import algohelper" in order to use it.')