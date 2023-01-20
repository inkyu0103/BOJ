import sys

input = sys.stdin.readline

N = int(input())
cur = N
dp = [0] * (10**6 + 1)

path = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    path[i] = i - 1
    if not i % 2 and dp[i] > dp[i // 2] + 1:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        path[i] = i // 2
    if not i % 3 and dp[i] > dp[i // 3] + 1:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        path[i] = i // 3


print(dp[N])

while True:
    print(cur, end=" ")
    if cur == 1:
        break
    cur = path[cur]
