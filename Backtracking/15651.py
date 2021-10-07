from itertools import product
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    for j in product(list(range(1,N+1)),repeat=M):
        print(*j)

def sol2():
    def dfs(depth):
        if depth == M:
            print(*result)
            return

        for target in range(1,N+1):
            result.append(target)
            dfs(depth+1)
            result.pop()

    N,M = map(int,input().split())
    result = []

    dfs(0)

sol2()