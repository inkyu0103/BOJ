# 2583  영역 구하기

import sys
from collections import deque

height , width , divide = map(int,sys.stdin.readline().split())
graph = [[0]*width for _ in range(height)]
visited = [[False]*width for _ in range(height)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]


for _ in range(divide):
    # 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
    # 2차원 배열로 벽 표현하기

    leftX, leftY ,rightX ,rightY = map(int,sys.stdin.readline().split())

    # y축은 아래를 기준으로 x축은 왼쪽을 기준으로 배열 인덱스에 접근하면 된다.

    leftY = height-leftY-1
    rightY = height-rightY

    for col in range(leftX, rightX):
        for row in range(rightY,leftY+1):
            graph[row][col] = 1


def find():
    for x in range(width):
        for y in range(height):
            if graph[y][x] == 0 and visited[y][x] == False:
                graph[y][x] = 1
                return y, x
    return -1


def bfs(startPoint):
    global room
    if startPoint == -1:
        return -1

    count = 1
    q = deque()

    q.append((startPoint[0],startPoint[1]))
    visited[startPoint[0]][startPoint[1]] = True

    while q:
        y,x = q.popleft()
        for move in dirs :
            newY = y+move[0]
            newX = x+move[1]


            if 0 <= newY < height and 0 <= newX < width and graph[newY][newX] == 0:
                visited[newY][newX] = True
                graph[newY][newX] = 1
                q.append((newY,newX))
                count += 1

    room += 1
    return count

box = []
room = 0

while 1:
    startPoint = find()

    if startPoint == -1:
        break
    box.append(bfs(startPoint))

print(room)
box.sort()
for x in box :
    print(x,end=" ")

