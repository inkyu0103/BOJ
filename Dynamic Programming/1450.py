import sys

N, K = map(int, sys.stdin.readline().split())

info = []
info.append([0, 0])
for i in range(N):
    m, v = map(int, sys.stdin.readline().split())
    info.append([m, v])

# info --> 무게 , 가치
# dyn[i][j] : 가방의 크기가 i일 때, j번 째 물건까지 담을 경우 최대 가치
dyn = [[0] * (N + 1) for i in range(K + 1)]

for k in range(1, K + 1):
    for n in range(1, N + 1):
        # 물건을 무거워서 못 담으면
        # n번째 물건보다 가방의 무게가 작으면 ,  이전 n-1번 째 물건을 담는걸로..
        if k < info[n][0]:
            # 가방 무게는 변하지 않고, 이거 안담을래
            dyn[k][n] = dyn[k][n - 1]
        # n번째 물건보다 가방의 무게가 크다면...
        else:
            dyn[k][n] = max(dyn[k][n - 1], dyn[k - info[n][0]][n - 1] + info[n][1])

print(dyn[K][N])