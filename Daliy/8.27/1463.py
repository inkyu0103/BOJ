# 1463 1로 만들기
dp = [0] *1000001

for i in range(2,1000001):
    if i % 2 == 0 and i % 3 != 0 :
        dp[i] = min(dp[i//2],dp[i-1]) + 1

    if i % 2 != 0 and i % 3 == 0 :
        dp[i] = min(dp[i//3],dp[i-1]) + 1

    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i//2],dp[i//3],dp[i-1]) + 1

    if i % 2 != 0 and i % 3 != 0:
        dp[i] = dp[i-1] + 1

N = int(input())
print(dp[N])
