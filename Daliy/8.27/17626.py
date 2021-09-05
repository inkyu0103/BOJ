# Four Squares
from math import sqrt,floor
import sys
def sol():
    dp = [0]*50001
    for i in range(1,224):
        dp[i**2] = 1

    for i in range(1,50001):
        if not dp[i]:
            min_val = sys.maxsize
            for k in range(1,floor(sqrt(i))+1):
                min_val = min(min_val,dp[i-k**2])
            dp[i] = min_val + 1

    user = int(input())
    print(dp[user])
sol()
