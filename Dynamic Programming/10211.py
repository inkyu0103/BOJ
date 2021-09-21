# Maximum Sybarray
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    N = int(input())
    arr = list(map(int,input().split()))

    dp = [0] * N
    dp[0] = arr[0]

    for i in range(1,N):
        if dp[i-1] + arr[i] > arr[i]:
            dp[i] = dp[i-1] + arr[i]

        else:
            dp[i] = arr[i]

    print(max(dp))

