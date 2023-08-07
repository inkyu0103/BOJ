# 17404 RGB거리 2

import sys
from math import inf

input = sys.stdin.readline


def sol():
    N = int(input())
    arr = [list(map(int, input().split(" "))) for _ in range(N)]
    answer = inf

    for i in range(3):
        dp = [[inf] * 3 for _ in range(N)]
        dp[0][i] = arr[0][i]

        for j in range(1, N):
            # 이전 칸이 red인 경우
            dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]

            # 이전 칸이 green인 경우
            dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]

            # 이전 칸이 blue인 경우
            dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]

        for k in range(3):
            if i != k:
                answer = min(answer, dp[-1][k])

    print(answer)


sol()
