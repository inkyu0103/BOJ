# 1106
from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = (100*1000)+1

def sol():
    C,N = map(int,input().split())
    dp = [0] * MAX
    dic = defaultdict(int)

    for _ in range(N):
        cost,cus = map(int,input().split())
        dic[cost] = cus

    keys = list(dic.keys())
    for i in range(1,MAX):
        for key in keys:
            if i-key >= 0:
                dp[i] = max(dp[i],dp[i-key]+dic[key])

    for idx,val in enumerate(dp):
        if val >=C:
            print(idx)
            break

    print(dp)
sol()
