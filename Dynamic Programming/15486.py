import sys

input = sys.stdin.readline

N = int(input())
T, P, dp = (
    [0] * 1500005,
    [0] * 1500005,
    [0] * 1500005,
)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

# print(T)
# print(P)
# print(dp)

for i in range(N, 0, -1):
    if i + T[i] <= N + 1:
        dp[i] = max(dp[i + T[i]] + P[i], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(max(dp))
