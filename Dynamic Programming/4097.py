# 4097
import sys
input = sys.stdin.readline

'''
처음 제출 반례 : -1,-2,-3,-4,-5 --> -1
dp[i] : i일에 얻을 수 있는 최대 수익.

dp[i] : 
'''

def sol():
    while 1:
        N =int(input())

        if N == 0:
            return

        price = []
        dp = []
        for _ in range(N):
            price.append(int(input()))
        dp.append(price[0])

        for i in range(1,N):
            dp.append(max(price[i],dp[i-1] + price[i]))

        print(max(dp))

sol()