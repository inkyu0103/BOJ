#4963 섬의 개수
#BFS /DFS 중 어느 것을 써야하나 약간 방의 개수 구하기 느낌인데
#readline()은 뒤의 공백까지 포함하므로 rsrtip을 써주자

import sys
from collections import deque

# (y,x)
dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

def findStart():
    for y in range(height):
        for x in range(width):
            if graph[y][x] == 1:
                start = (y,x)
                return start
    return -1

def BFS (start):
    queue = deque()
    #start point
    ty,tx = start
    graph[ty][tx] = 0
    queue.append(start)

    #BFS
    while queue:
        y,x = queue.popleft()

        for move in dirs:
            new_y , new_x = y + move[0], x +move[1]
            if 0 <=new_y <height and 0<= new_x < width and graph[new_y][new_x]:
                graph[new_y][new_x] = 0
                queue.append((new_y,new_x))

    return 1





while(1):

    val = sys.stdin.readline().rstrip()
    if val == "0 0":
        break

    else :
        count = 0
        width,height=map(int,val.split())
        graph = [list(map(int,sys.stdin.readline().split())) for _ in range(height)]

        while(1):
            val = findStart()
            if val == -1:
                print(count)
                break

            else :
                BFS(val)
                count += 1














