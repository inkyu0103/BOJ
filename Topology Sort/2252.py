#2252 줄 세우기

import sys

def DFS(start):
    visited[start] = True

    for x in graph[start]:
        if not visited[x]:
            DFS(x)

    sorting.append(start)


def DFSALL():
    for i in range(1,N+1):
        if not visited[i]:
            DFS(i)


N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
sorting =[]
visited = [False]*(N+1)
visited[0] =True

#Make Graph
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

DFS(1)
DFSALL()
sorting.reverse()

#역으로 들어가는 간선 여부 체크 안해도 되는건가?
for i in sorting:
    print(i,end=" ")