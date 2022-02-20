# 17198

import sys
from collections import deque
input = sys.stdin.readline

def get_start_loc(graph):
    for r in range(10):
        for c in range(10):
            if graph[r][c] == "B":
                return [r,c]

'''
def get_lake_loc(graph):
    for r in range(10):
        for c in range(10):
            if graph[r][c] == "L":
                return [r,c]

결국에는 L을 만났을 때 return을 해야하는데, 재귀적으로 호출하다보니, 그 상위 콜스택으로 return 하는 것
그렇게 되면 돌아올 수가 없게됨. (back tracking 이 불가)


그렇다면, 맨 마지막에서 L을 만나서 return 하는 값을 depth라고 하면,,,

def dfs(visit,graph,start_r,start_c,depth=1):
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    min_step = depth

    # 방문 표시
    visit[start_r][start_c] =1

    for dr,dc in dirs:
        new_r,new_c = start_r+dr,start_c+dc

        if 0<=new_r<10 and 0<=new_c<10 and not visit[new_r][new_c]:
            if graph[new_r][new_c] == '.':
                min_step = min(dfs(visit,graph,new_r,new_c,depth+1),min_step)

            if graph[new_r][new_c] == 'L':
                return depth

    visit[start_r][start_c] = 0
    return min_step
'''



def bfs(graph,start_r,start_c):
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([[start_r,start_c]])

    graph[start_r][start_c] = 0

    while queue:
        cur_r,cur_c = queue.popleft()

        for dr,dc in dirs:
            new_r,new_c = cur_r+dr, cur_c+dc

            if 0<=new_r<10 and 0<=new_c<10:
                if graph[new_r][new_c] == '.':
                    queue.append([new_r,new_c])
                    graph[new_r][new_c] = graph[cur_r][cur_c]+1

                elif graph[new_r][new_c] == 'L':
                    return graph[cur_r][cur_c]


def sol():
    graph = [list(input().strip()) for _ in range(10)]
    start_r,start_c = get_start_loc(graph)
    print(bfs(graph,start_r,start_c))

sol()
