# 11660 구간 합 구하기 5
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * ((N * N) + 1)
dp = [0] * ((N * N) + 1)

# 2차원 배열 -> 1차원 배열 변형
for i in range(N):
    for idx, val in enumerate(list(map(int, input().strip().split()))):
        arr[i * N + (idx + 1)] = val

dp[1] = arr[1]

# dp[i] = i번째 까지 숫자의 합
for i in range(2, ((N * N) + 1)):
    dp[i] = dp[i - 1] + arr[i]

# print(dp)
# 2차원 좌표 -> 1차원 좌표 -> 부분합
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split())
    ans = 0
    for x in range(x1, x2 + 1):
        start, end = N * (x - 1) + y1, N * (x - 1) + y2
        ans += dp[end] - dp[start - 1]
    print(ans)
