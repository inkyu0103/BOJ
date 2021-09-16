# 16918
from collections import deque
import sys
input = sys.stdin.readline

def sol():
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    R,C,N = map(int,input().split())
    graph = [list(input().strip()) for _ in range(R)]


    # 처음 그대로인 경우
    if N == 1:
        for arr in graph:
            print(*arr)
        return

    # 모두 꽉 찬경우
    elif N == 2:
        for _ in range(R):
            print('0'*C)
        return


    timer = [[0]*C for _ in range(R)]
    bomb = deque()
    for r in range(R):
        for c in range(C):
            # 3초에는 꽉 차있음.
            graph[r][c] = '0'
            if graph[r][c] =='0':
                timer[r][c] = 3
                bomb.append([r,c])

    initial_time = 3

    # initial_time == N 인 경우 탈출
    while initial_time < N:
        # 일단 터뜨리자.
        bomb_r,bomb_c = bomb.popleft()

        # 폭탄인 자리에 폭탄이 있다면, 터트리자.
        if timer[bomb_r][bomb_c] != 0:
            graph[bomb_r][bomb_c] ='.'
            timer[bomb_r][bomb_c] = 0

            for dr,dc in dirs:
                new_r,new_c = bomb_r+dr,bomb_c+dc

                if 0<=new_r<R and 0<=new_c<C:
                    graph[new_r][new_c] = '.'
                    timer[new_r][new_c] = 0

        # 다른 쪽에 의해서 이미 터진 경우는 빼자. (그냥 알아서 빠져나감)



sol()


