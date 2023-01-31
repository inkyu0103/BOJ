# 9466 텀 프로젝트
import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (N + 1)

    node_type = {
        "visited_node": 1,
        "nocycle_node": 2,
        "cycle_node": 3,
    }

    for i in range(1, N + 1):
        if arr[i] == i:
            visit[i] = node_type["cycle_node"]

    answer = N + 1

    def dfs(start):
        # 다음 노드를 방문하지 않은 경우
        if not visit[arr[start]]:
            print(visit)
            visit[start] = 1
            val = dfs(arr[start])

            # 사이클을 다 찾고 내려오는 경우
            if val == -1:
                return -1

            # 사이클의 시작과 같은 노드인 경우
            if val == start:
                print(f"val is {val}, start is{start}")
                visit[start] = 2
                return -1

            # 사이클에 포함된 노드인 경우
            if val != -1:
                visit[start] = 2
                return val
        # 다음 노드가 이미 방문된 경우 -> 이게 어디서 문제가 되냐면, 아예 방문하지 않은 노드를 새롭게 방문할 때 문제가 발생. 예제 첫번째 예시에서는 7번 노드 방문할때 3이 이미 방문되어있음
        else:
            # 단순 방문 -> 사이클이 맞는지 아닌지 확인해봐야함
            if visit[arr[start]] == node_type["visited_node"]:
                visit[start] = 2
                return arr[start]

            # 사이클이 아닌 노드 경우 or 이미 사이클인 경우
            else:
                visit[arr[start]]
                return -1

    for i in range(1, N + 1):
        if not visit[i]:
            visit[i] = node_type["visited_node"]
            dfs(i)

    print(visit)
