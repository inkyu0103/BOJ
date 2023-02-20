# 2011 암호코드
import sys

input = sys.stdin.readline

arr = [0] + list(map(int, list(input().rstrip())))
N = len(arr)
dp = [0] * N
dp[0] = 1
mod = 1000000

for i in range(1, N):
    if arr[i]:
        dp[i] = (dp[i - 1] + dp[i]) % mod

    case = arr[i - 1] * 10 + arr[i]
    if 10 <= case <= 26:
        dp[i] = (dp[i - 2] + dp[i]) % mod


print(dp[N - 1])
