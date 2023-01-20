import sys

input = sys.stdin.readline

T, W = map(int, input().split())
plum_trees = [int(input()) for _ in range(T)]

dp = [[0] * T for _ in range(W + 1)]

dp[0][0] = plum_trees[0] % 2
dp[1][0] = max((dp[0][0] + 1) % 2, dp[0][0])

for i in range(1, T):
    dp[0][i] = dp[0][i - 1] + plum_trees[i] % 2

for i in range(1, W + 1):
    for j in range(i, T):
        if plum_trees[j] % 2 == (i + 1) % 2:
            dp[i][j] = max(dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1, dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j])

print(dp[-1][-1])
