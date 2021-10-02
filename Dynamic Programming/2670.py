# 2670 연속 부분 최대 곱
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(float(input().strip()))
    dp =[0]*N
    dp[0] = arr[0]


    for i in range(1,N):
        dp[i] = max(arr[i] * dp[i-1],arr[i])

    print('%.3f' % round(max(dp),3))


sol()

