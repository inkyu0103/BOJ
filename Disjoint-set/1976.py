# 1976 여행가자. 문제를 잘못 이해했네

import sys
input = sys.stdin.readline

def find(node):
    global parent
    while(parent[node] != node):
        node = parent[node]
    return node


def union(a,b):
    global rank,parent
    a,b = find(a),find(b)
    if a==b:
        return;

    # 이제 b가 무조건 랭크가 높음
    if rank[a] > rank[b]:
        a,b = b,a
    parent[a] = b

    if rank[a] == rank[b]:
        rank[b] += 1

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [list(map(int,input().strip().split())) for _ in range(N)]

    parent = [i for i in range(N+1)]
    rank = [1] * (N + 1)

    for i in range(N):
        for j in range(i,N):
            if graph[i][j] == 1:
                union(i+1,j+1)

    route = list(map(int,input().strip().split()))
    flag = 0
    for i in range(len(route)-1):
        if find(route[i]) != find(route[i+1]):
            print("NO")
            flag = 1
            break
    if flag  == 0 :
        print("YES")








