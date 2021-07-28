# 13460 구슬탈출 2  / 시작 9시 / 1차 시도(30분) - 생각만 함. / 답보고 이해 (30분)
# 해답 봄 (3일 뒤 7/30일날 다시 풀 것)
# visit 배열의 존재 의미가 강구므.

from collections import deque
import sys
input = sys.stdin.readline


def find_loc ():
    R,B,O = (-1,-1),(-1,-1),(-1,-1)

    for n in range(N):
        for m in range(M):
            if graph[n][m] == "R":
                R = (n,m)
            elif graph[n][m] == "B":
                B = (n,m)
            elif graph[n][m] == "O":
                O = (n,m)

    return R,B,O


def BFS():
    q = deque()


def find_first(start):
    q=[]
    r,c = start
    for idx,content in enumerate(dirs):
        dr,dc = content
        new_r ,new_c = r+dr,c+dc

        if 0<=new_r<N and 0<=new_c<M and graph[new_r][new_c] == ".":
            q.append([idx,(new_r,new_c)])




if __name__ =='__main__':
    N,M = map(int,input().split())
    graph = [list(input().strip()) for _ in range(N)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,B,O = find_loc()



