# 2482 색상환

import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

dp = [[0] * 1002 for _ in range(1002)]

# 1개 고르는 경우
for i in range(1, N + 1):
    dp[i][1] = i


# 딱 절반인 경우
for i in range(4, N + 1, 2):
    dp[i][i // 2] = i // 2

# 나머지의 경우
for i in range(5, N + 1):
    for j in range(2, (i // 2) + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % 1000000003


print(dp[N][K])
