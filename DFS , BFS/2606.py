#2606 바이러스

def DFS(Start):
    global count
    count += 1
    Visited[Start - 1] = 1

    for i in range(Vertex):
        if (Matrix[Start - 1][i] == 1 and Visited[i] == 0):
            DFS(i + 1)


count = 0
Vertex = int(input())

Matrix = []
Visited = [0]*Vertex

for i in range(Vertex):
    Matrix.append(Vertex*[0])


Edge = int(input())

for i in range(Edge):
    row,col = map(int,input().split())
    row = row-1; col = col-1;

    Matrix[row][col] = 1 ; Matrix[col][row] = 1;

DFS(1)

print(count-1)

