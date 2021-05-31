# 7576 토마토
import sys
from collections import deque

def bfs():
    global Day
    queue = deque()
    for y in range(height):
        for x in range(width):
            # 처음에 익어 있는 토마토 정보를 큐에 담는다.
            if Tomato[y][x] == 1:
                queue.append((y,x))


    if len(queue) == 0:
        print(-1)
        return;

    last = queue[len(queue)-1]



    while queue:
        y,x = queue.popleft()
        Tomato[y][x] = 1

        for move in dirs:
            new_y , new_x = y + move[0] , x + move[1]
            if 0 <= new_y < height and 0 <= new_x < width and Tomato[new_y][new_x] == 0 :
                queue.append((new_y,new_x))
                Tomato[new_y][new_x] = 1

        if (y,x) == last and len(queue) > 0:
            Day += 1
            last = queue[len(queue)-1]



    # 전체 탐색
    for y in range(height):
        for x in range(width):
            if Tomato[y][x] == 0:
                print(-1)
                return ;
    print(Day)


width , height = map(int,sys.stdin.readline().split())
Tomato = [[int(i) for i in sys.stdin.readline().split()] for _ in range(height)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]  # 상 하 좌 우
Day = 0
bfs()

#인접 땅 정보
'''
-1 : 아무 것도 없는 땅
0  : 안 익은 토마토
1  : 익은 토마토
'''

