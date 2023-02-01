# 9657  돌 게임 3
import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * 1002

# dp[i] : 이기는 사람
dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 0
# print(dp[:10])


for i in range(5, N + 1):
    for j in [1, 3, 4]:
        if dp[i - j] == 1:
            dp[i] = 0
            break

        else:
            dp[i] = 1

print("CY" if dp[N] else "SK")
