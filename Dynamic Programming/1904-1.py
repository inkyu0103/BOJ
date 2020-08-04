# 1904 - memoization
# 재귀적 동적 계획법
# 재귀 깊이에 대한 제한이 있어서 못품

import time


start = time.time()
memo = {0:0,1:1}

def fibo(x):
    if x<2:
        return x

    else:
        if x not in memo:
            memo[x] = fibo(x-1)+fibo(x-2)
            return memo[x]

        else:
            return memo[x]

N = int(input())

print(fibo((N+1)%15746))

end = time.time()
print(end-start)






