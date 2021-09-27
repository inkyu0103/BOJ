# 중량제한
# 이분탐색 + BFS
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    # 간선 정보 그래프에 입력
    for _ in range(M):
        start,end,wei = map(int,input().split())
        graph[start].append([wei,end])
        graph[end].append([wei,start])

    start,end = map(int,input().split())


    def bfs(weight):
        q = deque()
        q.append(start)
        visit = [0] * (N+1)
        # start 는 방문
        visit[start] = 1

        while q:
            # 근데 여기서 한 번 방문 했다고, 곧바로 종료하면 안된다. 그 이유는, 한 경우가 방문에 성공하였다 해서,
            # 반드시 제시된 weight를 넘었다고 볼 수 있다는 보장 x --> 반례 만들어보자.
            cur_city = q.popleft()

            for next_wei,next_city in graph[cur_city]:
                if next_wei >= weight and not visit[next_city]:
                    q.append(next_city)
                    visit[next_city] = 1
        return True if visit[end] else False

    # 이분 탐색에 필요한 최소, 최대 범위
    _min, _max = 1,1000000000
    result = _min

    while _min<=_max:

        mid = (_min + _max) // 2

        if bfs(mid):
            result = mid
            _min = mid+1

        else:
            _max = mid-1

    print(result)
sol()

