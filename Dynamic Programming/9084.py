# 9084 동전
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coin_type = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target + 1)
    dp[0] = 1

    for t in coin_type:
        for i in range(1, target + 1):
            if i >= t:
                dp[i] += dp[i - t]

    print(dp[target])
