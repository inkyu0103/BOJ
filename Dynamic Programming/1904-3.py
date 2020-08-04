
import sys
sys.setrecursionlimit(10000)

def fibo(n, __cache={0: 0, 1: 1}):
    """Get nth fibonacci number"""
    if n in __cache:
        return __cache[n]%15746

    __cache[n] = fibo(n-1) + fibo(n-2)
    return __cache[n]%15746

N = int(input())

print(fibo(N%15746))