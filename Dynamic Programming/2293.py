# 2293
import sys
input = sys.stdin.readline

'''
그 값을 만들 수 있는 경우의 수!
'''

def sol():
    n,k = map(int,input().split())
    coins = []
    dp = [0] * (k+1)
    dp[0] = 1

    for _ in range(n):
        coins.append(int(input()))

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i-coin]



    print(dp[k])





sol()