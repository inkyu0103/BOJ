# 11660 구간 합 구하기 복습
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]


# dp table 셋업
for r in range(N):
    for c in range(N):
        if c == 0:
            dp[r][c] = arr[r][c]
            continue

        dp[r][c] = dp[r][c - 1] + arr[r][c]

for i in dp:
    print(i)

answer = 0
for _ in range(M):
    x1, y1, x2, y2 = list(map(lambda x: int(x) - 1, input().split()))

    if y1 == 0:
        for r in range(x1,x2+1):
            answer +=  dp[r][N-1]

    else:
        for r in range(x1,x2+1):
            answer +=

