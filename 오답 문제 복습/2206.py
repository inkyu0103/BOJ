#벽 부수고 이동하기

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    dist_arr = [[0]*M for _ in range(N)]
    # 깬 벽돌 수, 거리, 좌표 r , 좌표 c
    q = deque([(0,1,0,0)])
    dist_arr[0][0] = 1

    while q:

        break_blocks,dist,cur_r,cur_c = q.popleft()


        for dr,dc in dirs:
            new_dist,new_r,new_c = dist+1,cur_r+dr,cur_c+dc

            if 0<=new_r<N and 0<=new_c<M and (not dist_arr[new_r][new_c] or dist_arr[new_r][new_c] > new_dist):
                if graph[new_r][new_c]=='0':
                    q.appendleft((break_blocks,new_dist,new_r,new_c))
                    dist_arr[new_r][new_c] = new_dist

                else:
                    if break_blocks<K:
                        q.append((break_blocks+1,new_dist,new_r,new_c))
                        dist_arr[new_r][new_c] = new_dist


    return dist_arr[N-1][M-1] if dist_arr[N-1][M-1] else -1


N,M,K = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
dirs =[(0,1),(0,-1),(1,0),(-1,0)]
print(bfs())

