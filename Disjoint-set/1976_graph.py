# 1976 그래프 버전
# 플로이드 - 워셜?

import sys
from collections import deque
input = sys.stdin.readline
INF = 1e19


def bfs(start,target):
    global graph,N
    visit = []
    q = deque()
    q.append(start)

    while(q):
        idx = q.popleft()
        if idx == target:
            return 1
        if idx not in visit:
            visit.append(idx)
            for i in graph:
                for j in range(N):
                    if i[j] == 1:
                        q.append(j+1)

    return 0


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [list(map(int,input().strip().split())) for _ in range(N)]
    route = list(map(int,input().strip().split()))
    flag = 0
    for i in range(len(route)-1):
        if bfs(route[i],route[i+1])==0:
            print("NO")
            flag = 1
            break
    if flag == 0:
        print("YES")





