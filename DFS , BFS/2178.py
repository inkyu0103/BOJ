#2178 미로탐색
import sys
from collections import deque

#함수
def dfs():
    global count

    # (y,x)로 넣을 겁니다.
    # 한 개의 vertex를 pop 할 때 추가되는 vertex의 마지막 아이를 기억해 놨다가, 그 아이가 pop 되면 거리를 1 늘리는 방식을 택했습니다.
    queue = deque()
    lastPoint = (0,0)

    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        if (y, x) == lastPoint or  (y,x) == end:
            count += 1


        if (y,x) == end:
            print(count)
            return ;

        Maps[y][x] = 0
        for move in dirs:
            new_y, new_x = y + move[0], x + move[1]
            if 0 <= new_y < height and 0 <= new_x < width and Maps[new_y][new_x]:
                queue.append((new_y, new_x))
                Maps[new_y][new_x] = 0

                #만약 lastpoint에 대한 노드들이 추가가 된다면 lastpoint를 수정해준다.

        if (y,x) == lastPoint and len(queue)>=1:
            lastPoint = queue[len(queue)-1]






# 메인
# Bfs는 모든 간선을 다 한번씩 돌아다니기 때문에 최단 거리로 도착 가능

height , width = map(int,sys.stdin.readline().split())
Maps = [[int(i) for i in sys.stdin.readline().rstrip('\n')] for i in range(height)]
count = 0
end = (height-1,width-1)
dirs = [(1,0),(-1,0),(0,1),(0,-1)] #하 상 우 좌

dfs()



















