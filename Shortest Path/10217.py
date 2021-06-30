# 10217 KCM Travel
# 비용이 자연수 && 1번 --> N 번 노드까지의 최단 경로
'''
    LA에 도착할 수 없는 경우
        1. 경로가 없다
        2. 돈이 없다

    주의 할 점 : A->B로 가는 항공편이 항상 하나라는 보장이 없다 --> 최솟값만 받자
    time을 최소로 해야할지... cost를 최소로 해야할지... 아니면 그냥 다 받아도 되나? 덮어씌우기 하면 되니까
'''

import sys
import heapq
import sys

MAX = 1e20
testCase = int(sys.stdin.readline())

for t in range(testCase):
    airport , money , info = map(int,sys.stdin.readline().split())


    Time = [MAX for _ in range(airport)]
    graph = [[] for _ in range(airport)]
    All = [[] for _ in range(airport)]

    for i in range(info):
        # s : start / e : end / c :consume money / time
        s, e, c, time = map(int,sys.stdin.readline().split())
        graph[s].append([time,c,e])

def dijkstra():
    q = []
    # q append form : time, cost, end
    q.append([0,0,0])

    while q:
        time , cost , ed = heapq.heappop(q)

        for nTime , nCost , nEd in graph[ed]:
            nTime += time
            nCost += cost
            if (nTime > Time[time]):
                Time[nEd] = nTime
                All[nEd].append([nTime,nCost])
                heapq.heappush(q,[nTime,nCost,nEd])
