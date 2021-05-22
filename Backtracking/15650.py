# 15650
from itertools import combinations

def sol():
    N,M = map(int,input().split())
    for i in combinations(range(1,N+1),M):
        print(*i)
sol()
