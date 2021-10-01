# 14494
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    dp = [[1]*M for _ in range(N)]

    for i in range(1,N):
        for j in range(1,M):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1])%1000000007


    print(dp[N-1][M-1]%1000000007)

sol()