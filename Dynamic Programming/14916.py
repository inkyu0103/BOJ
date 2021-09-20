# 14916 거스름 돈
import math
n = int(input())
INF = math.inf

dp = [0]*(100001)
dp[2],dp[4],dp[5] = 1,2,1
for i in range(6,n+1):
    a,b = math.inf,math.inf
    if dp[i-2]:
        a=dp[i-2]+1
    if dp[i-5]:
        b=dp[i-5]+1
    dp[i] = min(a,b)

print(dp[n] if dp[n] else -1)