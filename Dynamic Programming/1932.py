#1932 정수 삼각형

import sys

def solve ():
    for i in range(testCase):
        for j in range(i+1):

            #기저 케이스
            if i == 0:
                dp[i][j] = cost[i][j]
                continue

            # i가 두번 째 줄부터는 j의 인덱스에 따라 j-1 , j 중에서 최대 값을 더해 나간다.
            if j == 0 :
                dp[i][j] = cost[i][j] + dp[i-1][j]
                continue

            if i == j :
                dp[i][j] = cost[i][j] + dp[i-1][j-1]
                continue

            dp[i][j] = cost[i][j] + max(dp[i-1][j-1],dp[i-1][j])

    return max(dp[testCase-1])


testCase = int(input())
#초기화
cost = [[-1]*testCase for i in range(testCase)]
for i in range(testCase):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(0,i+1):
        cost[i][j] = tmp[j]

#Memo
dp = [[-1]*testCase for i in range(testCase)]

print(solve())



