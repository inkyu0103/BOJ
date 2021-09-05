# 1389 케빈 베이컨의 6단계 법칙
# 정신이 아득하네.
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visit = [0] * (N+1)
    q = deque([[0,start]])

    while q:
        cur_step,cur_node = q.popleft()

        for next_node in graph[cur_node]:
            if not visit[next_node]:
                visit[next_node] = cur_step + 1
                q.append([cur_step+1,next_node])
    return sum(visit)



N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
sum_step = sys.maxsize
answer = -1



for _ in range(M):
    s,e= map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,N+1):
    val = bfs(i)
    if sum_step > val:
        answer = i
        sum_step = val
    elif sum_step == val:
        answer = min(answer,i)


print(answer)



