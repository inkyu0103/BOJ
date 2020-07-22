#5567 결혼식

import sys


def DFS():
    global count
    # 상근이의 직접적인 친구  / 상근이는 1번
    for x in range(people+1):
        if (graph[1][x]) == 1:
            Visited[x] = 1
            check.append(x)



    # 친구의 친구
    for x in check:
        for i in range(2,people+1):
            if Visited[i] != 1 and graph[x][i] == 1:
                Visited[i] = 1



people = int(input())
listLength = int(input())

graph = [[0]*(people+1) for _ in range(people+1)]
Visited = [0]*(people+1)
check = []


for i in range(listLength):
    st,ed = map(int,sys.stdin.readline().split())
    graph[st][ed] = 1
    graph[ed][st] = 1

DFS()


print(Visited.count(1))