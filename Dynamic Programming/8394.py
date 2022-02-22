# 8394

'''
악수를 안 할 수도 있음
p(n)을 n명일 때 악수하는 횟수라 하자.

n = 1 --> p(1) = 1
n = 2 --> p(1) + 1 = 2  . .
n = 3 --> p(2) + 1 = 3
n = 4 --> p(3) +        . . . .

'''
import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] % 10 + dp[i - 2] % 10
    print(dp[-1] % 10)
sol()
