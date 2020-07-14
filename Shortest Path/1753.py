#1753 최단경로
'''
다익스트라 알고리즘
'''

import sys
import math
import heapq

INF = math.inf

V, E = map(int,sys.stdin.readline().split())
Start_vertex = int(input())
Map = [[]*V for _ in range(V+1)]
# d : distance / p : previous / v : visit

d=[INF]*(V+1)
d[Start_vertex] = 0
q=[]

# 그래프 완성
# 다른 방식으로도 입력 할 수 있구나.
for i in range(E):
    S , L , W = map(int,sys.stdin.readline().split())
    Map[S].append([L,W])


#cost, node
heapq.heappush(q,[0,Start_vertex])
while q:
    cost , node = heapq.heappop(q)
    for n, c in Map[node]:
        c += cost
        if c < d[n]:
            d[n] = c
            heapq.heappush(q,[c,n])

for i in range(1,len(d)):
    if d[i] == INF :
        print("INF")
    else:
        print(d[i])