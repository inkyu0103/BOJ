# 15654
import sys
input = sys.stdin.readline

def sol():
    def dfs(depth):
        if depth == M:
            print(*result)
            return

        for target in range(1,N+1):
            if not visit[target]:
                visit[target] = 1
                result.append(arr[target-1])
                dfs(depth+1)

                visit[target] = 0
                result.pop()

    N,M = map(int,input().split())
    result = []
    visit = [0] * (N+1)
    arr = list(map(int,input().split()))
    arr.sort()

    dfs(0)


sol()