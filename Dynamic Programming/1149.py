#1149 RGB 거리

import sys

def solve(arr):
    for i in range(len(data)):
        if i == 0 :
            dp[i][0] = arr[0][0]
            dp[i][1] = arr[0][1]
            dp[i][2] = arr[0][2]
            continue

        # Red
        dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])

        # Green
        dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])

        # Blue
        dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])

    minVal = min(dp[len(arr)-1][0],dp[len(arr)-1][1],dp[len(arr)-1][2])

    return minVal



houseNum = int(input())
dp = [[-1]*3 for _ in range(houseNum)]

# 입력받기
data = [list(map(int,sys.stdin.readline().split())) for _  in range(houseNum)]

print(solve(data))




