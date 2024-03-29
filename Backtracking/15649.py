#15649 N과 M (1)

from itertools import permutations
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    arr = [i for i in range(1,N+1)]
    for i in permutations(arr,M):
        for j in i:
            print(j,end=" ")
        print()


def sol2():
    def dfs(depth):
        if depth == M:
            print(*result)
            return

        for target in range(1,N+1):
            if not visit[target]:
                result.append(target)
                visit[target] = 1

                dfs(depth+1)

                result.pop()
                visit[target] = 0


    N,M = map(int,input().split())
    visit = [0] * (N+1)
    result = []

    dfs(0)

sol2()

