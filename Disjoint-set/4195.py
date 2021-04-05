# 4195 친구 네트워크
import sys
input = sys.stdin.readline

def find(node):

    while(parent[node] != node):
        node = parent[node]
    return node


def union(a,b):
    global rank, parent
    a,b = find(a),find(b)

    if a == b :
        return;

    if rank[a] > rank[b]:
        a,b = b,a
    parent[a] = b
    rank[b] += 1

    if rank[a] == rank[b] :
        rank[b] +=1


if __name__ == "__main__":
    tc = int(input())
    for i in range(tc):
        network = int(input())
        rank = {}
        parent = {}

        for j in range(network):
            a,b = map(str,input().strip().split())

            if a not in parent and b not in parent:
                parent[a] = a
                parent[b] = b
                rank[a] = 1
                rank[b] = 1
                print(rank[a]+rank[b])
                union(a,b)

            elif a not in parent and b in parent:
                parent[a] = a
                rank[a] = 1
                print(rank[find(b)] + rank[a])
                union(a,b)

            elif a in parent and b not in parent:
                parent[b] = b
                rank[b] = 1
                print(rank[find(a)] + rank[b])
                union(a,b)
