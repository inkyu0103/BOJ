# 11055 가장 큰 증가 부분 수열 (복습)
'''
결국 for문 2번 도네...
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
dp = [i for i in arr]

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + arr[i], dp[i])

print(max(dp))


