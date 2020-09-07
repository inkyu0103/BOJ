#11052 카드 구매하기

N = int(input())
costs = [0]
costs += list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = costs[1]
dp[2] = max(costs[2], costs[1]*2)

for i in range(3, N+1):
    dp[i] = costs[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])