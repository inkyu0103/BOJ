# 3372

import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]

    dp[0][0] = 1

    for r in range(N):
        for c in range(N):
            jump = board[r][c]

            if not jump:
                continue

            if r+jump < N:
                dp[r+jump][c] += dp[r][c]

            if c+jump < N:
                dp[r][c+jump] += dp[r][c]

    print(dp[N-1][N-1])

sol()