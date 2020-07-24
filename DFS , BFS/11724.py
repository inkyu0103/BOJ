#11724 연결 요소의 개수
# 희소한 그래프의 경우에는 인접리스트가 훨씬 빠르다

import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    for i in range(vertex):
        if graph[start][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)


vertex, edge = map(int,sys.stdin.readline().split())
graph =[[0]*vertex for _ in range(vertex)]
visit = [0]*vertex
count = 0

for _ in range(edge):
    st,ed = map(int,sys.stdin.readline().split())
    graph[st-1][ed-1] = 1
    graph[ed-1][st-1] = 1

for i in range(vertex):
    if visit[i] == 0:
        count += 1
        dfs(i)


print(count)




