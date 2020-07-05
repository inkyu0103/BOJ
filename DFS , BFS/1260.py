#1260 DFS BFS

def DFS(StartVertex):
    print(StartVertex , end=" ")
    visited_arr[StartVertex-1] = 1

    for i in range(V):
        if(matrix[StartVertex-1][i] == 1 and visited_arr[i] == 0):
            DFS(i+1)

def BFS(StartVertex):
    queue_for_BFS.append(StartVertex)
    visited_arr[StartVertex-1] = 1

    while(1):
        val = queue_for_BFS.pop(0)
        print(val , end=" ")

        for i in range(V):
            if (matrix[val-1][i]==1 and visited_arr[i] == 0):
                queue_for_BFS.append(i+1)
                visited_arr[i] = 1

        if (len(queue_for_BFS) == 0):
            break



#V : vertex , E : edge , S : start vertex

V, E, S = map(int,input().split())

visited_arr = [0] * V
matrix =[]
queue_for_BFS = []  #시간이 많이 걸리려나?

# V*V matrix
for i in range(V):
    matrix.append([0]*V)


for i in range(E):
    row, col = map(int,input().split())
    row = row-1; col = col -1

    # 간선 연결
    matrix[row][col] = 1; matrix[col][row] = 1;

DFS(S)

# 초기화
visited_arr = [0] * V
print()

BFS(S)





