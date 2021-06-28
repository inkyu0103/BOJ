# 10282
# a가 b에 의존하고 있다. b --> a로 가는 간선 O
# 같은 의존성 2번 존재 x 보통 같은 간선이 여러개 주어지고 가중치만 다른 경우에는 최적값으로 갱신해야함.
# 마지막 컴퓨터가 감염되기까지의 시간.
# 아 s가 0도 포함이구나

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0

    while q:
        wei,curNode = heapq.heappop(q)
        if dist[curNode] < wei:
            continue
        for n in graph[curNode]:
            nextWei,nextNode = n
            newWei = nextWei + wei

            if dist[nextNode] > newWei:
                dist[nextNode] = newWei
                heapq.heappush(q,(newWei,nextNode))


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        # n : 컴퓨터 대수 , d : 의존성 개수, c: 해킹당한 컴퓨터 / 일단 자기 자신은 감염됨
        answer = 0
        time = 0
        n,d,c = map(int,input().split())
        graph = [[] for _ in range(n+1)]
        dist = [sys.maxsize] * (n+1)

        for _ in range(d):
            a,b,s = map(int,input().split())
            # 가중치 , 노드
            graph[b].append((s,a))

        dijkstra(c)
        for i in range(1,len(dist)):
            if dist[i] != sys.maxsize:
                answer += 1
                time = max(time,dist[i])
        print("{} {}".format(answer,time))
