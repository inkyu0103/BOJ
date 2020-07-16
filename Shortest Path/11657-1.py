#11657 벨만 포드였군요
import sys
import math

INF = math.inf

N,M = map(int,sys.stdin.readline().split())
graph = [[INF]*N for _ in range(N)]
dist = [[INF]*N for _ in range(N+1)]

for _ in range(M):
    # A : 시작 도시, B : 끝 도시 , C : 가중치
    A,B,C = map(int,sys.stdin.readline().split())
    if graph[B-1][A-1] > C:
        graph[B-1][A-1] = C


# d(v,0) v == s 이면 0 , v != s 이면 INF
#d(s,0) =0 초기화

dist[0][0] = 0

def Bellman_Ford():

    for k in range(1,N+1):
        for v in range(N):
            dist[k][v] = dist[k-1][v]
            for w in range(len(graph[v])):
                if graph[v][w] != 0 :
                    if dist[k-1][w] + graph[v][w] < dist[k][v]:
                        dist[k][v] = dist[k-1][w] + graph[v][w]
        if dist[k-1] == dist[k]:
            for i in range(1,len(dist[k])):
                if dist[k][i] == INF :
                    print(-1)
                else:
                    print(dist[k][i])
            return ;

    print(-1)
    return

Bellman_Ford()








