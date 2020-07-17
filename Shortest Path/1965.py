#1965 운동

#플로이드 같어

import sys
import math
INF = math.inf

V , E  =map(int,sys.stdin.readline().split())
graph = [[INF]*V for _ in range(V)]


for _ in range(E):
    st, ed , cost = map(int,sys.stdin.readline().split())
    if graph[st-1][ed-1] > cost:
        graph[st-1][ed-1] = cost

for i in range(V):
    graph[i][i] = 0


def Floyd ():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


def Check():
    Min = INF
    for s in range(V):
        for e in range(V):
            if s == e :
                continue
            if Min > graph[s][e]+graph[e][s]:
                Min = graph[s][e]+graph[e][s]

    if Min == INF:
        print(-1)
    else:
        print(Min)



Floyd()
Check()
