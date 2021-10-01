# 14430
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    dp = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i-1>=0 and j-1>=0:
                dp[i][j] += max(dp[i-1][j] , dp[i][j-1])
                continue

            if i-1>=0:
                dp[i][j] += dp[i-1][j]
                continue

            if j-1>=0:
                dp[i][j] += dp[i][j-1]
                continue

    print(dp[N-1][M-1])
sol()