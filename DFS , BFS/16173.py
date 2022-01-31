# 16173 jump king jelly
from collections import deque
import sys
input = sys.stdin.readline

def bfs(N:int,jump_info:list):
    # jump_dist, curR,curC
    dirs = [[1,0],[0,1]]
    queue = deque([[jump_info[0][0],0,0]])

    visit = [[0]*N for _ in range(N)]
    visit[0][0] = 1
    end_point = [N-1,N-1]

    while queue:
        jump_dist,cur_r,cur_c = queue.popleft()
        for dr,dc in dirs:
            new_r,new_c = cur_r+dr*jump_dist, cur_c+dc*jump_dist

            if [new_r,new_c] == end_point:
                return "HaruHaru"

            if 0<=new_r<N and 0<=new_c<N and not visit[new_r][new_c]:
                visit[new_r][new_c] = 1
                queue.append([jump_info[new_r][new_c],new_r,new_c])

    return "Hing"


def sol():
    N = int(input())
    jump_info = [list(map(int,input().split())) for _ in range(N)]
    print(bfs(N,jump_info))

sol()
