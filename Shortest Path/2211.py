# 2211 네트워크 복구 (시작시간 1시 46분 / 25분 지났네)

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra ():
    # time , node
    q = [(0,1)]
    ck = [0]*(N+1)

    while q:
        cur_time , cur_node = heapq.heappop(q)

        if cur_time > dist[cur_node]:
            continue

        for next_time,next_node in graph[cur_node]:
            new_time = next_time + dist[cur_node]
            if dist[next_node] > new_time:
                dist[next_node] = new_time
                heapq.heappush(q,(new_time,next_node))

                #새로 거리가 갱신이 되면 경로를 업데이트 해주자.
                ck[next_node] = cur_node

                # 1번이 무조건 출발이니까

    return ck

if __name__=='__main__':
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    path = [[0]*(N+1) for _ in range(N+1)]
    dist = [INF] * (N+1)
    dist[1] = 0

    for _ in range(M):
        s,e,t = map(int,input().split())

        # 양방향 그래프
        graph[s].append((t,e))
        graph[e].append((t,s))


    ck = dijkstra()
    print(N-1)
    for i in range(2,N+1):
        print(i,ck[i])


