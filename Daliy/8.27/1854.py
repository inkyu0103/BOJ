# K번째 최단 경로 찾기 / max heap이 필요한듯
# visit 배열이 필요한가? 체크를 하게 되면 안될 거 같은데... 아니면 5번 미만이라는 조건을 달고 나와야 할 수도?
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    q = [[0,1]]

    while q:
        curCost,curNode = heapq.heappop(q)

        for n in graph[curNode]:
            addCost,nextNode = n
            newCost = curCost+addCost


            if len(each_city_queue[nextNode]) < k:
                heapq.heappush(each_city_queue[nextNode],-newCost)
                heapq.heappush(q, [newCost, nextNode])

            # 왜 최대값을 갱신하는지 생각해보세요~ each_city_queue[nextNode]에 값이 없는 경우에 오류가 발생할 수 있다.

            elif heapq.nsmallest(1,each_city_queue[nextNode])[0] * -1 > newCost:
                heapq.heappop(q)
                heapq.heappush(q,-newCost)

            print(each_city_queue)


n,m,k = map(int,input().split())

each_city_queue = defaultdict(list)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append([cost,e])


# 초기화
for i in range(1,n+1):
    each_city_queue[i]


dijkstra()
for i in each_city_queue:
    if len(each_city_queue[i]) < k:
        print(-1)
    else:
        print(-heapq.heappop(each_city_queue[i]))
