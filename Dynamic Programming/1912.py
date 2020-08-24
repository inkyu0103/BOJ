# 연속합

num = int(input())
base = list(map(int,input().split()))
dp =[0]*num
dp[0] = base[0]

for i in range(1,len(base)):
    if base[i] > dp[i-1] + base[i]:
        dp[i] = base[i]
    else:
        dp[i] = dp[i-1] + base[i]

print(max(dp))
