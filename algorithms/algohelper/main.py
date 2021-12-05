from time import time
from memory_profiler import memory_usage

def exectime(function):
    start = time()
    function()
    end = time()
    return end - start

def maxmemusage(function):
    usage = memory_usage(function)
    maxmemusage = max(usage)
    return maxmemusage

def avgmemusage(function):
    usage = memory_usage(function)
    avgmemusage = sum(usage) / len(usage)
    return avgmemusage


if __name__ == '__main__':
    print('import this file via "import algohelper" in order to use it.')