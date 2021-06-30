# 4485 그래프 모양에서의 다익스트라. 근데 생각해보면 주위의 정점을 둘러보는건 마찬가지

import sys
input = sys.stdin.readline
import heapq

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def dijkstra(N,dp,graph):
    q = [(graph[0][0],0,0)]

    while q:
        curLoss, r,c = heapq.heappop(q)

        for mv in dirs:
            newR,newC = mv[0] + r , mv[1] + c

            if 0<=newR<N and 0<=newC<N:
                if dp[newR][newC] == -1:
                    newLoss = curLoss + graph[newR][newC]
                    dp[newR][newC] = newLoss
                    heapq.heappush(q,(newLoss,newR,newC))

                # 방문이 되어있는 경우
                else:
                    if dp[newR][newC] > curLoss + graph[newR][newC] :
                        newLoss = curLoss + graph[newR][newC]
                        dp[newR][newC] = newLoss
                        heapq.heappush(q,(newLoss,newR,newC))


def sol():
    count = 1
    while(1):

        N = int(input())

        if N == 0:
            return

        graph = [list(map(int, input().split())) for _ in range(N)]
        lossRupee = [[-1] * N for _ in range(N)]
        lossRupee[0][0] = graph[0][0]

        dijkstra(N,lossRupee,graph)
        print("Problem {}: {}".format(count,lossRupee[N-1][N-1]))
        count += 1

sol()
