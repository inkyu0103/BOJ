# 2206 벽 부수고 이동하기
'''
    1개의 벽을 부수는거야?
'''

import sys
from collections import deque

# 지도
height , width = map(int, sys.stdin.readline().split())
Map = [[int(i) for i in sys.stdin.readline().rstrip('\n')] for _ in range(height)]
Visit = [[[-1]*2 for i in range(width)] for i in range(height)]


#(y,x) 상 하 좌 우
dirs = [(-1,0),(1,0),(0,-1),(0,1)]


#bfs

'''
3번째 차수의 값이 0이면 벽을 부술 수 있음
3번째 차수의 값이 1이면 이미 벽을 부숨 
'''
def bfs():
    queue = deque()

    queue.append((0,0,0))
    Visit[0][0][0] = 1



    while queue:
        y,x,z = queue.popleft()

        for move in dirs:
            new_y , new_x = y+move[0] , x+move[1]

            if 0 <= new_y < height and 0 <= new_x < width:
                #원래의 길이면 얘가 벽을 부쉈던 아니던 상관이 없다.
                if Map[new_y][new_x] == 0 and Visit[new_y][new_x][z] == -1:
                    queue.append((new_y,new_x,z))
                    Visit[new_y][new_x][z] = Visit[y][x][z] + 1
                #길을 뚫어야 하는 경우면 벽을 부수지 않은 경우만 가능하다
                elif z == 0 and Map[new_y][new_x] == 1 and Visit[new_y][new_x][z+1] == -1:
                    queue.append((new_y,new_x,z+1))
                    Visit[new_y][new_x][z+1] = Visit[y][x][z] + 1


bfs()

if Visit[height-1][width-1][0] == -1:
    print(Visit[height-1][width-1][1])

elif Visit[height-1][width-1][1] == -1:
    print(Visit[height-1][width-1][0])

else:
    print(min(Visit[height-1][width-1][1],Visit[height-1][width-1][0]))








'''
1) 길이 없다는 것을 어떻게 판단할 것인가?
이거는 B의 값으로 판단하면 된다.

2) 어느 벽을 부술 것인가?
--> 이게 문제인데, 먼저 break의 여부를 물어보고,  0이면, 그 위치에서 갈 수 있는 모든 좌표는 열여준다.
--> 1이면 어림도 없지 ㅋ

3) 오... 3차원으로 하는구나
visit 에 대한 리스트도 따로 만들어서 관리
'''

