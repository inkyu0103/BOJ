#11727

case = int(input())

dp= [0,1,3]

for i in range(3,1001):
    dp.append((dp[i-1]+dp[i-2]*2)%10007)

print(dp[case])