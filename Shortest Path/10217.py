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
MAX = 1e20
testCase = int(input())
for t in range(testCase):
    airport , money , info = map(int,sys.stdin.readline().split())


    #시간 초기화
    T = [MAX]*airport
    T[0]=0

    All = [[] for _ in range(airport)]

    # s : start / e : end / c :consume money / time
    graph = [[] for _ in range(airport)]
    for i in range(info):
        s, e, c, time = map(int,sys.stdin.readline().split())
        graph[s].append([time,c,e])

# q append form : time, cost, end
def dijkstra():
    q = []
    q.append([0,0,0])

    while q:
        time , cost , ed = heapq.heappop(q)

        #graph에는 [time, cost, ed] 순으로 되어있다.
        for nTime,nCost,nEd in graph[ed]:
          nTime += time
          if T[nEd] > nTime:
              T[nEd] = nTime
              nCost += cost
              heapq.heappush(q,[nTime,nCost,ed])












