# 7562 나이트의 이동
from collections import deque

dirs = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
tc = int(input())


for i in range(tc):
    q = deque()
    # 한 변의 길이
    l = int(input())
    #현재 위치

    m =[[0]*l for i in range(l)]
    t = [[False]*l for i in range(l)]

    cx,cy = map(int,input().split())
    # 가고자하는 위치
    dx,dy = map(int,input().split())

    q.append((cx,cy))

    while q:

        x,y = q.popleft()

        if (x,y) == (dx,dy):
            break

        for move in dirs :
            newX = x+move[0]
            newY = y+move[1]

            #범위 안에 있다면
            if 0<= newX <l and 0<=newY <l and t[newX][newY] == False:
                if m[newX][newY] == 0:
                    m[newX][newY] = m[x][y]+1

                q.append((newX,newY))
                t[newX][newY] = True

    print(m[dx][dy])






