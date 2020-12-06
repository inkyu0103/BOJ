# 11403 경로 찾기

import sys
n = int(input())
g =[]

#그래프 완성
for i in range(n):
    g.append(list(map(int,sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] == 1 and g[k][j] == 1:
                g[i][j] = 1

for i in range(n):
    for j in range(n):
        print(g[i][j],end=" ")
    print()