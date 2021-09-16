# 17471 (1시 10분 ~ )

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
INF = sys.maxsize

def sol():
    # part = 1 : 지역구 1, part = 0 : 지역구 0
    def bfs(start,part):
        q = deque([start])
        visit[start] = 1

        while q:
            cur_node = q.popleft()
            for next_node in graph[cur_node]:
                if part and next_node in part1 and not visit[next_node]:
                    q.append(next_node)
                    visit[next_node] = 1

                elif not part and next_node not in part1 and not visit[next_node]:
                    q.append(next_node)
                    visit[next_node] = 1


    N = int(input())
    people = [0] + list(map(int,input().split()))

    graph = [[] for _ in range(N+1)]

    for i in range(1,N+1):
        adj_num , *adj_node = map(int,input().split())
        graph[i] = adj_node

    no_case_flag = 1
    answer = INF
    for c in range(1,N):
        # 여기서 지역구 1과 지역구 2를 bfs를 돌면서 인접했는지 확인하자.
        for part1 in combinations(range(1,N+1),c):
            part2 = []
            for i in range(1,N+1):
                if i not in part1:
                    part2.append(i)
            part1 = list(part1)

            visit = [0] * (N+1)
            bfs(part1[0],1)
            bfs(part2[0],0)

            # 모든 노드를 방문한 경우
            if visit.count(0) == 1:
                no_case_flag = 0

                part1_people = sum([ people[i] for i in part1 ])
                part2_people = sum(people) - part1_people


                answer = min(answer,abs(part1_people-part2_people))

    if no_case_flag == 1:
        print(-1)
    else:
        print(answer)
sol()
