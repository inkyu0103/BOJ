#삼각 달팽이

N = int(input())
graph = [[0]*(N+2) for _ in range(N+2)]

x,y,num = 0,1,0
count = (N*(N+1))//2
print(count)

# padding
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or i == N+1:
            graph[i][j] = -1
        else:
            if j == 0 or j == N+1:
                graph[i][j] = -1


while(num <count):
    #하
    while(graph[x+1][y] == 0):
        print("하")
        num += 1
        graph[x+1][y] = num
        x+=1

    #우
    while(graph[x][y+1] == 0):
        print("우")
        num += 1
        graph[x][y+1] = num
        y+=1

    #대각

    while(graph[x-1][y-1] == 0):
        print("대각")
        num +=1
        graph[x-1][y-1] = num
        x-=1
        y-=1

for i in graph:
    print(i)
