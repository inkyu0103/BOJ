# 6059
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize


def BFS(N,start,end):
    visit = [0] *(N+1)
    dp = [0] *(N+1)

    visit[start] = 1


    q = deque([(0,start)])

    while q:
        cur_length , cur_node = q.popleft()

        for n in tree[cur_node]:
            next_length,next_node = n

            if not visit[next_node]:
                visit[next_node] = 1
                dp[next_node] = dp[cur_node] + next_length
                q.append((dp[next_node],next_node))

    return dp[end]

if __name__ =='__main__':
    N,Q = map(int,input().split())
    tree = [[] for _ in range(N+1)]

    for _ in range(N-1):
        s,e,c = map(int,input().split())
        tree[s].append((c,e))
        tree[e].append((c,s))

    for _ in range(Q):
        s,e = map(int,input().split())
        print(BFS(N,s,e))