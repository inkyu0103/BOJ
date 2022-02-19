# 16395
import sys
input = sys.stdin.readline

def generate_memo ():
    memo = [[1]*30 for _ in range(30)]
    for r in range(30):
        for c in range(1,r):
            memo[r][c] = memo[r-1][c-1] + memo[r-1][c]
    return memo

def sol():
    memo = generate_memo()
    n,k = map(int,input().split())
    print(memo[n-1][k-1])

sol()
