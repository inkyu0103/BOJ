from itertools import product

def sol():
    N,M = map(int,input().split())
    for j in product(list(range(1,N+1)),repeat=M):
        print(*j)
sol()