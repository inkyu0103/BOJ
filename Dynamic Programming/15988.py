#15988
import sys
input = sys.stdin.readline

def sol():
    dp = [0]*(1000001)
    dp[1],dp[2],dp[3] = 1,2,4


    tc = int(input())
    arr = [int(input()) for _ in range(tc)]
    for i in range(4,max(arr)+1):
        dp[i] = (dp[i-3]+dp[i-2]+dp[i-1])%1000000009

    for i in arr:
        print(dp[i])

sol()