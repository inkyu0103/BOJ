# 1106
from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = (100*1000)+1

def sol():
    C,N = map(int,input().split())
    dp = [0] * MAX
    dic = []

    for _ in range(N):
        cost,cus = map(int,input().split())
        dic.append([cost,cus])


    # 아 이게 dict로 받으면 같은 key가 들어올때 처리를 못하는구나?

    for i in range(1,MAX):
        for cost,cus in dic:
            if i-cost >= 0:
                dp[i] = max(dp[i],dp[i-cost]+cus)

    for idx,val in enumerate(dp):
        if val >=C:
            print(idx)
            break


sol()
