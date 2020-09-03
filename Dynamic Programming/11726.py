#11726

case = int(input())
dp = [1,2,3]

for i in range(3,1001):
    dp.append((dp[i-1]+dp[i-2])%10007)

print(dp[case-1])

