# 11060
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [INF]*N
    dp[0] = 0

    for i in range(N):
        for j in range(1,arr[i]+1):
            if i+j < N:
                dp[i+j] = min(dp[i+j],dp[i]+1)

    print(dp[-1] if dp[-1] != INF else -1)

sol()
