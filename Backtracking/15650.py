# 15650
from itertools import combinations
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    for i in combinations(range(1,N+1),M):
        print(*i)

def sol2():
    def dfs(depth,before):
        if depth == M:
            print(*result)
            return

        for target in range(1,N+1):
            if not visit[target] and target > before:
                result.append(target)
                visit[target] = 1

                dfs(depth+1,target)

                result.pop()
                visit[target] = 0


    N,M = map(int,input().split())
    visit = [0] * (N+1)
    result = []

    dfs(0,0)


sol2()