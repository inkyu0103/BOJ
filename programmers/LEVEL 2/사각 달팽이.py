N = int(input())

graph = [[0]*(N+2) for _ in range(N+2)]
x,y,num = 1,1,1
graph[1][1] = 1

#벽 만들기
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or i == N+1:
            graph[i][j] = -1
        else:
            graph[i][0] = -1
            graph[i][N+1] = -1

for i in graph:
    print(i)
#채우기

while(num<N**2):
    #하
    while(graph[x+1][y] == 0):

        num += 1
        graph[x+1][y] = num
        x += 1
    #우
    while(graph[x][y+1] == 0):

        num += 1
        graph[x][y+1] = num
        y+=1

    #상
    while(graph[x-1][y] == 0):
        print("C")
        num += 1
        graph[x-1][y] = num
        x -= 1

    #좌
    while(graph[x][y-1]== 0 ):
        num += 1
        graph[x][y-1] = num
        y -= 1



for i in graph:
    print(i)