#계단 오르기
# 증명을 하고 싶다
import sys

stairs = int(input())
dp = [0 for i in range(stairs+1)]
cost = [int(sys.stdin.readline()) for _ in range(stairs)]
cost.insert(0,0)


'''
아... dp배열의 인덱스에 거기에 갈 수 있는 모든 경우를 생각해서 max를 때리면 되는구나
'''
if stairs == 1:
    print(dp[1])

else:
    dp[1] = cost[1]
    dp[2] = max(cost[1]+cost[2], cost[2])
    dp[3] = max(cost[2]+cost[3], cost[1]+cost[3])

    for i in range(4,stairs+1):
        dp[i] = max(dp[i-3]+cost[i-1]+cost[i] , dp[i-2]+cost[i])


    print(dp[stairs])