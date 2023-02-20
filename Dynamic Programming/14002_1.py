# 14002 가장 긴 증가하는 부분 수열 4
import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * 1001
prev = [0] * (N + 1)
answer = []


for i in range(1, N + 1):
    for j in range(i, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

maxi, maxd = 1, dp[1]

for i in range(2, N + 1):
    if maxd < dp[i]:
        maxi = i
        maxd = dp[i]

cur = maxi

while cur:
    answer.append(arr[cur])
    cur = prev[cur]

print(len(answer))
print(*reversed(answer))
