# 2667 단지 번호 붙이기

import sys
from collections import deque

# (y,x)
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs (start):
    count = 1
    queue = deque()
    queue.append(start)

    while queue:
        x,y = queue.popleft()
        Maps[y][x] = 0

        for move in dirs:
            new_x , new_y = x+move[1] , y+move[0]

            if 0<=new_x< len(Maps[0]) and 0 <=new_y<testCase and Maps[new_y][new_x]:
                queue.append((new_x,new_y))
                Maps[new_y][new_x] = 0
                count += 1

    count_box.append(count)
    return 1





testCase = int(sys.stdin.readline())
group = 0
count_box = []

# 하하 뿌듯하군요
Maps=[[int(i) for i in sys.stdin.readline().rstrip('\n')] for _ in range(testCase)]

for y in range(testCase):
    for x in range(len(Maps[0])):
        if Maps[y][x] == 1 :
            group += bfs((x,y))

print(group)
count_box.sort()
for i in count_box:
    print(i)