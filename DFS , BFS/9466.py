# 9466 텀 프로젝트

import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (N + 1)

    for i in range(1, N + 1):
        if not visit[i]:
            q = deque([i])
            visit[i] = 1

            while q:
                cur_node = q.pop()

                # 현재 노드가 2라면... 다음 노드도 확인해 볼 필요가 있음
                if visit[cur_node] == 2:
                    # 사이클 다음 노드가 visit 값이 1인 상태라면? 추가
                    if visit[arr[cur_node]] == 1:
                        visit[arr[cur_node]] = 2
                        q.append(arr[cur_node])
                    continue

                # 일반적인 방문
                visit[cur_node] = 1

                # 다음 노드 추가 근데 이런 방식으로 하면, 이전 노드들을 표시할 수가 없음.
                if not visit[arr[cur_node]]:
                    q.append(arr[cur_node])
                    visit[arr[cur_node]] = 1

                # 어? 이미 방문한 노드네?
                elif visit[arr[cur_node]] == 1:
                    q.append(arr[cur_node])
                    visit[arr[cur_node]] = 2

                # 사이클 직전 노드라면... 뭐 할게 더 있냐 -> 확인해보고 삭제제
                elif visit[arr[cur_node]] == 2:
                    pass

    print(visit)
