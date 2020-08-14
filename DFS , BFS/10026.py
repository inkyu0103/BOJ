# 10026

import sys
from collections import deque

def BFS(start,arr,v):
    q = deque()
    q.append(start)


    while q:
        y,x = q.popleft()

        for move in dirs:
            newY = y+move[0]; newX = x+move[0]
            if 0 <= newY < areaNum and 0<= newX < areaNum and arr[newY][newX]==v:
                q.append((newY,newX))

    return 1


def find(arr):
    for y in range(areaNum):
        for x in range(areaNum):
            if arr[y][x] != 0:
                return (y,x,arr[y][x])
    return -1


dirs =[(1,0),(-1,0),(0,1),(0,-1)]
areaNum = int(input())
area1 = [[i for i in sys.stdin.readline().rstrip()] for _ in range(areaNum)]
area2 = [[0]*areaNum for _ in range(areaNum)]


#적록색약 세팅
for i in range(areaNum):
    for j in range(areaNum):
        if area1[i][j] == "R" or area1[i][j] == "G":
            area2[i][j] = 1
count1=0
while 1:
    val = find(area1)
    if val == -1 :
        break
    y=val[0]; x=val[1]; value = val[2];
    count1+=BFS((y,x),area1,value)



print(count1)






