# 15990
from collections import defaultdict
import sys
input = sys.stdin.readline

def sol():
    tc = int(input())
    a = defaultdict(lambda: [0, 0, 0])

    arr = [int(input()) for _ in range(tc)]
    dp = [0] *(max(arr)+1)
    dp[1],dp[2],dp[3] = 1,1,3
    a[1],a[2],a[3] = [1,0,0],[0,1,0],[1,1,1]

    for i in range(4,max(arr)+1):
        a[i][0] = (a[i-1][1] + a[i-1][2])%1000000009
        a[i][1] = (a[i-2][0] + a[i-2][2])%1000000009
        a[i][2] = (a[i-3][0] + a[i-3][1])%1000000009

        dp[i] = sum(a[i])

    for i in arr:
        print(dp[i]%1000000009)
    print(a)

sol()
