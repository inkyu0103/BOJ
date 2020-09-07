#14501 퇴사

import sys

days = int(input())

graph = [[0]*days for _ in range(2)]
dp = [0]*25

for i in range(days):
    t,p = map(int,sys.stdin.readline().split())
    graph[0][i] = t
    graph[1][i] = p

for i in range(days):
    if dp[i] > dp[i+1] :
        dp[i+1] = dp[i]

    if dp[i+graph[0][i]] < dp[i] + graph[1][i] :
        dp[i + graph[0][i]] = dp[i] + graph[1][i]

print(dp[days])