# 1660
import bisect
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    N = int(input())
    size = []
    i = 0

    while (i*(i+1)*(i+2)//6) <= 300000:
        size.append(i*(i+1)*(i+2)//6)
        i+=1


    dp = [1]*(N+1)
    dp[0] = 0

    for i in range(1,N+1):
        dp[i] = INF
        j=1
        while i - size[j] >=0:
            dp[i] = min(dp[i],dp[i-size[j]]+1)
            j+=1

    print(dp[N])







sol()