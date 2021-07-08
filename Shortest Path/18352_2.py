# 18352 BFS로 가능한지? 그랴... 줄어들었네...
import sys
from collections import deque
input = sys.stdin.readline


def BFS(N,start_node,target_dist):
    q = deque()
    q.append(start_node)
    answer = []
    level = 0

    # 없으면 사이클이 발생하는 경우 무한 루프가 돌게 될 듯
    visit = [0]*(N+1)
    visit[start_node] = 1

    # 각 처음 노드에서 몇 번째 레벨에 도달하였는지 체크하기 위한 아이들
    count = 0
    length = 1

    while q:
        cur_node = q.popleft()
        count += 1

        for next_node in graph[cur_node]:
            if not visit[next_node]:
                q.append(next_node)
                visit[next_node] = 1

                if level + 1 == target_dist:
                    answer.append(next_node)

        if count == length:
            count = 0
            length = len(q)
            level += 1

    answer.sort()

    return answer

if __name__ == '__main__':
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for m in range(M):
        s,e = map(int,input().split())
        graph[s].append(e)

    answer = BFS(N,X,K)

    if not answer:
        print(-1)

    for i in answer:
        print(i)
