# 2294
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    n,k = map(int,input().split())
    coins = []
    dp = [INF] * (k+1)
    dp[0] = 0

    for _ in range(n):
        coins.append(int(input()))

    for i in range(1,k+1):
        for coin in coins:
            if i-coin>=0:
                dp[i] = min(dp[i],dp[i-coin] + 1)

    print(dp[k] if dp[k] != INF else -1)
sol()
