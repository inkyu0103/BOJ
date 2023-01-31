import sys

input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
TC = int(input())
dp = [[0] * 2010 for _ in range(2010)]

# dp 초기화
for i in range(1, N + 1):
    dp[i][i] = 1
    if numbers[i] == numbers[i - 1]:
        dp[i - 1][i] = 1

for dist in range(2, N):
    for i in range(1, N - dist + 1):
        s, e = i, i + dist
        if numbers[s] == numbers[e] and dp[s + 1][e - 1]:
            dp[s][e] = 1

for _ in range(TC):
    s, e = map(int, input().split())
    print(dp[s][e])
