# 1005 ACM Craft
import sys
import copy
from collections import deque

input = sys.stdin.readline


def sol():
    T = int(input())

    for _ in range(T):
        # N : 건물 개수, K 규칙 개수
        N, K = map(int, input().split())
        costs = [0] + list(map(int, input().split()))
        cumulative_costs = copy.deepcopy(costs)
        graph = [[] for _ in range(N + 1)]
        answer = 0

        # 간선 정보를 거꾸로 등록
        for _ in range(K):
            s, e = map(int, input().split(" "))
            graph[e].append(s)

        target_building = int(input())

        # 타겟 빌딩부터 시작
        q = deque()
        q.append(target_building)

        while q:
            cur_building = q.popleft()

            if not graph[cur_building]:
                answer = max(answer, cumulative_costs[cur_building])
                continue

            # 진행할 건물이 있는 경우
            for next_building in graph[cur_building]:
                if (
                    cumulative_costs[cur_building] + costs[next_building]
                    > cumulative_costs[next_building]
                ):
                    cumulative_costs[next_building] = (
                        cumulative_costs[cur_building] + costs[next_building]
                    )

                    q.append(next_building)

        print(answer)


sol()
