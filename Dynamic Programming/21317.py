# 21317 징검다리 건너기 (8시 20분)
# dp[i] = min(dp[i-2] + arr[i][1],dp[i-1] + arr[i][0], dp[i-3]+k) 이게 점화식 같은데

import sys
input = sys.stdin.readline

N = int(input())
step = [[0,0]]
dp = [0]*N

for _ in range(N-1):
    step.append(list(map(int,input().split())))
k = int(input())

isUse = 0
for i in range(1,N):
    print(i)
    if i == 1:
        dp[i] = step[i][0]

    elif i == 2:
        dp[i] = min(dp[i-1] + step[i][0], dp[i-2]+step[i][1])

    else:
        if isUse == 0:
            print((dp[i-1],step[i][0]), (dp[i-2],step[i][1]),(dp[i-3],k))
            if dp[i-3]+k == min(dp[i-1]+step[i][0], dp[i-2]+step[i][1],dp[i-3]+k):
                dp[i] = dp[i-3]+k
                isUse = 1
            else:
                dp[i] = min(dp[i-1]+step[i][0], dp[i-2]+step[i][1])
        else:
            dp[i] = min(dp[i-1]+step[i][0], dp[i-2]+step[i][1])

print(dp)
print(dp[N-1])



