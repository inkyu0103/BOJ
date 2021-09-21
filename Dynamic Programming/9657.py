# 돌 게임 3
import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(N+1)
dp[1] = 1; dp[2] = 2;dp[3] = 1;dp[4]= 1

for i in range(1,N+1):
    if not dp[i]:
        dp[i] = min(dp[i-1]+1,dp[i-3]+1,dp[i-4]+1)

print(dp[N])
print("SK" if dp[N]%2 else "CY")