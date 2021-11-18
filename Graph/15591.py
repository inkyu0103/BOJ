# 15591
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize


def sol():
    def bfs(start,k):
        visit = [0] * (N+1)
        q = deque()
        q.append([INF,start])
        visit[start] = 1

        recommend_count = 0

        while q:
            USADO,cur_node = q.popleft()

            for next_USADO,next_node in _map[cur_node]:
                if not visit[next_node] and min(USADO,next_USADO) >=k:
                    recommend_count  += 1
                    q.append([min(USADO,next_USADO),next_node])
                    visit[next_node] = 1

        return recommend_count

    N,Q = map(int,input().split())
    _map = [[] for _ in range(N+1)]

    for _ in range(N-1):
        p,q,r = map(int,input().split())
        _map[p].append([r,q])
        _map[q].append([r,p])

    for _ in range(Q):
        k,v = map(int,input().split())
        print(bfs(v,k))


sol()