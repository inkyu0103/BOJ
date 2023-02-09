# 14002 가장 긴 증가하는 부분 수열 4

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]
trace = [0] * (N + 1)

# dp 초기화
for i in range(1, N + 1):
    dp[1][i] = 1

# dp 테이블 채우기
for i in range(2, N + 1):
    for j in range(i, N + 1):
        for k in range(i, j):
            if arr[j] > arr[k]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + 1)
            elif arr[j] < arr[k]:
                print(i, j, k)

                dp[i][j] = 1
for i in dp:
    print(i)
