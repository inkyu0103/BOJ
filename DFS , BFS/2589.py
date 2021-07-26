# 2589 시작시간 11시 05분 ~ 1차 시도 시간 11시 21분 (시간초과)
# 2~3차시도 ~12시

'''
보물은 최단거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
이동은 육지로만 가능.
그럼 육지로만 다 이동하는 케이스를 봐야하나?
bfs를 통해서 최대 어디까지 갈 수 있는지 알아보면 되지 않을까

필요한 것

1. Land 위치 찾기
2. BFS / DFS를 통해 쭉쭉 늘어나기.

find --> bfs

첫 수정
흠... visit 배열이 필요없는가?
dfs가 더 빠른가?
graph를 돌때 시작점...?
아 그리고 단순히 bfs는 안되는구나

'''

import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

def BFS(start,R,C):
    q = deque([start])
    max_dist = 0

    while q:
        r,c = q.popleft()

        for d in dirs:
            dr ,dc = d
            new_r,new_c =r+dr,c+dc
            if 0<=new_r<R and 0<=new_c<C and visit[new_r][new_c] == 0 and graph[new_r][new_c] != "W":
                visit[new_r][new_c] = 1
                graph[new_r][new_c] = graph[r][c] + 1
                max_dist = max(max_dist,graph[new_r][new_c])
                q.append((new_r,new_c))

    return max_dist

if __name__ =="__main__":
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,C =  map(int,input().split())
    graph = [list(input().strip()) for _ in range(R)]
    answer = 0

    for r in range(R):
        for c in range(C):
            if graph[r][c] != "W":
                visit = [[0]*C for _ in range(R)]
                graph[r][c] = 0
                visit[r][c] = 1
                answer = max(answer,BFS((r,c),R,C))

    print(answer)

