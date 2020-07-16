#11404

import sys
MAX = 1e19
cites = int(sys.stdin.readline())
bus = int(sys.stdin.readline())

graph =[[MAX]*cites for _ in range(cites)]
#초기화
for _ in range(cites):
    graph[_][_] = 0

#최소값만 받도록 하자.
for b in range(bus):
    st , ed, cost =map(int, sys.stdin.readline().split())
    if graph[st-1][ed-1] > cost:
        graph[st - 1][ed - 1] = cost

def Floyd ():
    for k in range(cites):
        for i in range(cites):
            for j in range(cites):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    #return
    for x in range(cites):
        for y in range(cites):
            if graph[x][y] ==MAX:
                print(0 , end=" ")
            else :
                print(graph[x][y] , end=" ")
        print()

Floyd()



