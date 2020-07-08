#1012
import sys
from collections import deque

def bfs(start,maps):
    queue = deque()
    queue.append(start)

    while queue:
        y,x = queue.popleft()
        maps[y][x] = 0

        for move in dirs:
            new_y, new_x = y+move[0], x+move[1]

            if 0<= new_y < height and 0<= new_x < width and Matrix[new_y][new_x]:
                queue.append((new_y,new_x))
                maps[new_y][new_x] = 0


    return 1



dirs = [(1,0),(-1,0),(0,1),(0,-1)]

testCase = int(input())

for i in range(testCase):

    width,height,n = map(int,sys.stdin.readline().split())
    Matrix = [[0 for _ in range(width)] for _ in range(height)]
    # 지도 만들기
    #for j in range(height):
    #    Matrix.append([0]*width)

    # 배추정보 입력하기
    for k in range(n):
        x,y = map(int,sys.stdin.readline().split())
        Matrix[y][x] = 1
    count = 0
    for y in range(height):
        for x in range(width):
            if Matrix[y][x] == 1:
                count += bfs((y,x),Matrix)

    print (count)
