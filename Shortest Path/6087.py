# 6087 시작 10시 6분 / 고민 30분 / 답안 25분 / 11시 16분 끝

from collections import deque
import sys
import math
input = sys.stdin.readline
INF = sys.maxsize


def find_light ():
    light = []
    for w in range(W):
        for h in range(H):
            if graph[h][w] =="C":
                light.append((h,w))
    return light

def bfs(sh,sw):
    q = deque([(sh,sw)])
    visit = [[INF]*W for _ in range(H)]
    visit[sh][sw] = 0

    while q:
        h,w = q.popleft()

        for dh,dw in dirs:
            new_h,new_w = h+dh,w+dw

            while 1:
                # 범위를 벗어난 경우
                if not(0<=new_h<H and 0<=new_w<W):break
                # 벽과 부딪힌 경우
                if graph[new_h][new_w] == "*":break
                # 더 늦게 방문한 경우
                if visit[new_h][new_w] < visit[h][w] + 1:break

                q.append((new_h,new_w))
                visit[new_h][new_w] = visit[h][w] + 1
                new_h += dh
                new_w += dw

    print(visit[eh][ew]-1)


if __name__ =='__main__':
    W,H = map(int,input().split())
    graph = [list(input().strip()) for _ in range(H)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    (sh,sw),(eh,ew) = find_light()

    bfs(sh,sw)






