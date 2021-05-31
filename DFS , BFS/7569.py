#7569 토마토 3차원

import sys
from collections import deque

garo , sero , height = map(int,sys.stdin.readline().split())
Tomato = [[[int(i) for i in sys.stdin.readline().split()] for _ in range(sero)] for _ in range(height)]
# (z,y,x) 상 하 판에서 위 / 판에서 아래 / 좌 우
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
Day = 0


def bfs():
    global Day
    queue = deque()
    for z in range(height):
        for y in range(sero):
            for x in range(garo):
                if Tomato[z][y][x] == 1 :
                    queue.append((z,y,x))

    if len(queue) == 0:
        print(-1)
        return;
    lastPoint = queue[len(queue)-1]

    while queue:
        z,y,x = queue.popleft()
        Tomato[z][y][x] = 1

        for move in dirs:
            new_z, new_y ,new_x = z+move[0] , y+move[1] , x+move[2]

            if 0 <= new_z < height and 0 <= new_y < sero and 0 <= new_x < garo and Tomato[new_z][new_y][new_x] == 0:
                queue.append((new_z,new_y,new_x))
                Tomato[new_z][new_y][new_x] = 1

        if lastPoint == (z,y,x) and len(queue) > 0 :
            Day += 1
            lastPoint = queue[len(queue)-1]

# 전체 탐색
    for z in range(height):
        for y in range(sero):
            for x in range(garo):
                if Tomato[z][y][x] == 0 :
                    print(-1)
                    return ;

    print(Day)



bfs()