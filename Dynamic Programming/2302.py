# 2302 극장 좌석

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
vips = [0] + [int(input()) for _ in range(M)]
vips.append(N + 1)

# print(vips)
dp = [0] * 41
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

# print(dp)
answer = 1

for i in range(1, len(vips)):
    answer *= dp[vips[i] - vips[i - 1] - 1]

print(answer)
