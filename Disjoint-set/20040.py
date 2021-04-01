# 20040 사이클 게임

import sys
input = sys.stdin.readline

def find(node):
    global parent
    while(node!=parent[node]):
        node= parent[node]
    return node

def union(a,b):
    global rank, parent
    a,b = find(a),find(b)

    if a == b :
        return 1

    if rank[a] > rank[b] :
        # 이제 무조건 b가 랭크가 더 큼
       a,b = b,a
    parent[a] = b

    if rank[a]== rank[b]:
        rank[b] += 1




if __name__ == "__main__":
    N, M = map(int,input().split())
    parent = [i for i in range(N)]
    rank = [1]*N
    flag = 0
    for i in range(M):
        a,b = map(int,input().split())
        check = union(a,b)
        if check == 1:
            flag = 1
            print(i+1)
            break

    if flag == 0:
        print(0)
