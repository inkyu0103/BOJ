# 1446
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    q = [(0,0)]

    while(q):
        curDist,curNode = heapq.heappop(q)
        if dp[curNode] < curDist :
            continue

        else:

            for nextNode in graph[curNode]:
                newDist = curDist + graph[curNode][nextNode]

                if dp[nextNode] > newDist:
                    dp[nextNode] = newDist

                    if nextNode in graph:
                        heapq.heappush(q,(newDist,nextNode))


if __name__ == '__main__':
    N,D = map(int,input().split())
    graph = dict()
    dp = {}
    for _ in range(N):
        s,e,dist = map(int,input().split())
        if s<=D and e <=D:
            dp[s],dp[e] = INF,INF
            # 처음 생성되는 경우
            if s not in graph:
                graph[s] ={e:dist}

            #존재 하는 경우 --> 최솟값 갱신
            else:
                graph[s][e] = min(graph[s][e], dist)

    dp[0] = 0
    dijkstra()
    min_dist = INF
    for target in dp:
        min_dist = min(min_dist,dp[target]+D-target)
    print(graph)
    print(dp)
    print(min_dist)












