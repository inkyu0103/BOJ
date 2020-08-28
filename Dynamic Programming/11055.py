#11055 가장 큰 증가 부분 수열
num = int(input())
arr = list(map(int,input().split()))
dp  = [i for i in arr]


def solve():
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] :
                dp[i] = max(arr[i] + dp[j],dp[i])


solve()
print(max(dp))