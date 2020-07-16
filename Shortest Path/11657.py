#11657 타임머신

import sys

#N : 도시의 개수 ,  M : 버스 노선의 개수

def Floyd():
    global graph
    for k in range(N):
        for i in range(N):
            for j in range( N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


N,M = map(int,sys.stdin.readline().split())
INF = 100000000
graph = [[INF]*N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0


for _ in range(M):
    # A : 시작 도시, B : 끝 도시 , C : 가중치
    A,B,C = map(int,sys.stdin.readline().split())
    graph[A-1][B-1] = C

Floyd()

for i in range(1,N):
    if graph[0][0] < 0:
        print(-1)
        break

    if graph[0][i] == INF:
        print(-1)

    else:
        print(graph[0][i])

