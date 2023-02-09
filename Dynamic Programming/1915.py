# 1915 가장 큰 정사각형
import sys
from math import sqrt

input = sys.stdin.readline


N, M = map(int, input().split())
square = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
answer = 0


for r in range(N):
    for c in range(M):
        if r == 0 or c == 0:
            dp[r][c] = square[r][c]
        elif not square[r][c]:
            dp[r][c] = 0
        else:
            dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1

        answer = max(answer, dp[r][c])

print(answer**2)
