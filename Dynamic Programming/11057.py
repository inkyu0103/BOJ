#11057 오르막 수

num = int(input())
g = [[1]*10 for i in range(1000)]

for i in range(1,1000):
    for j in range(10):
        tmp = 0
        for k in range(j,10):
            tmp += g[i-1][k]
        g[i][j] = tmp


print(sum(g[num-1])%100007)

