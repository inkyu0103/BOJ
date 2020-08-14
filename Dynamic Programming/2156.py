# 2156 포도주 시식

'''
1. 어떻게 연속 3잔인걸 아니?
    인덱스를 보고 옆에있으면 depth+1 하다가
    depth가 3이되면 return 0을 해줄까?

'''



num = int(input())
wei = [0]
dp =[0]
for i in range(num):
    wei.append(int(input()))
dp.append(wei[1])

if num >1 :
    dp.append(wei[1]+wei[2])
for i in range(3,num+1):
    dp.append(max(dp[i-1],dp[i-3]+wei[i-1]+wei[i],dp[i-2]+wei[i]))

print(dp[num])


