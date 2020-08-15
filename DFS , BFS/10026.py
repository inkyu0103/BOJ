# 10026

import sys
from collections import deque

def BFS(start,arr,v):
    q = deque()
    q.append(start)

    while q:
        y,x = q.popleft()
        arr[y][x] = -1

        for move in dirs:
            newY = y+move[0]; newX = x+move[1]

            if 0 <= newY < areaNum and 0<= newX < areaNum and arr[newY][newX] == v:
                q.append((newY,newX))
    return 1


def find(arr):
    for y in range(areaNum):
        for x in range(areaNum):
            if arr[y][x] != -1:
                return (y,x,arr[y][x])

    return -1


dirs =[(1,0),(-1,0),(0,1),(0,-1)]
areaNum = int(input())
area1=[]
area2 = [[0]*areaNum for _ in range(areaNum)]


for i in range(areaNum):
    area1.append(list(map(str,input())))

#적록색약 세팅
for i in range(areaNum):
    for j in range(areaNum):
        if area1[i][j] == "R" or area1[i][j] == "G":
            area2[i][j] = 1


count1=0
count2=0

for i in range(areaNum):
    for j in range(areaNum):
        if area1[i][j] != -1:
            BFS((i,j),area1,area1[i][j])
            count1 +=1
        if area2[i][j] != -1:
            BFS((i,j),area2,area2[i][j])
            count2+=1



print("{} {}".format(count1,count2))







