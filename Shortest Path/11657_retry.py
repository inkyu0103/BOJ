#11657 타임머신

import sys
import math
import copy
INF = math.inf
city , road = map(int,input().split())

graph = [[0]*city for i in range(city)]
dist = [INF]*city
dist[0] = 0
edges =[]

for i in range(road):
    start , end , wei = map(int,sys.stdin.readline().split())
    graph[start-1][end-1] = wei
    edges.append((start,end,wei))


for i in range(city-1): # 반복
    for edge in edges:
        if dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
            dist[edge[1]-1] = dist[edge[0]-1] + edge[2]

tmp = copy.copy(dist)

for edge in edges:
    if dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
        dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]

if dist != tmp:
    print(-1)

else:
    for i in range(1,len(tmp)):
        if tmp[i] != INF:
            print(tmp[i])

        else:
            print(-1)


