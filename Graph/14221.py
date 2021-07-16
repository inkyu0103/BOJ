# 14221 편의점
# 양방향 간선
# 문제는 모든 집 후보를 루트로 다익스트라를 돌려야 하냐? 라는 문제이다.
# 누가 더 빠를까? 벨만 포드 vs 다익스트라 n 회 --> 시간 초과
# 집 기준 말고 어차피 양방향이니까 편의점 기준에서 재면 안될까? ㅇㅇ 안됨
# 잘 생각해보면 음의 간선이 없기 때문에 간선을 추가하면 더 증가하는 경우밖에 없음
'''
생각했던 건, 만약 2번 부터 편의점까지의 거리는 1번에서

'''


import sys
import heapq
INF = sys.maxsize

def dijkstra(n,start):
    dist_dp = [INF]*(n+1)
    dist_dp[start] = 0

    q = [(0,start)]


    while q:
        cur_wei , cur_node = heapq.heappop(q)
        if dist_dp[cur_node] < cur_wei:
            continue

        for n in graph[cur_node]:
            next_wei, next_node = n

            new_wei = cur_wei + next_wei

            if dist_dp[next_node] > new_wei:
                dist_dp[next_node] = new_wei
                heapq.heappush(q,(new_wei,next_node))

    return dist_dp




if __name__ == '__main__':
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s,e,c = map(int,input().split())
        graph[s].append((c,e))
        graph[e].append((c,s))

    # p : 집 / q : 편의점
    p,q = map(int,input().split())
    home_candidate = list(map(int,input().strip().split()))
    store_candidate = list(map(int,input().strip().split()))

    target = 0
    tmp_cost = INF

    for start in store_candidate:
        dist_dp = dijkstra(n,start)

        for home in home_candidate:
            if tmp_cost > dist_dp[home]:
                tmp_cost = dist_dp[home]
                target = home
            elif tmp_cost == dist_dp[home]:
                target = min(target,home)

    print(target)







