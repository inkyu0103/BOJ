# 15652
import sys
input = sys.stdin.readline

# 중복조합으로 풀어도 되는 것이다.
def sol1():
    def dfs(depth,before):
        if depth == M:
            print(*result)
            return

        for target in range(1,N+1):
            if target >= before:
                result.append(target)
                dfs(depth+1,target)
                result.pop()

    N,M = map(int,input().split())
    result = []
    dfs(0,0)


sol1()
