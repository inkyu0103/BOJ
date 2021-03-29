# 1717 집합의 표현
import sys
input = sys.stdin.readline

def find(node):
    global nodes
    while(nodes[node] != node):
        node = nodes[node]
    return node

def merge(a,b):
    global rank,nodes
    a,b = find(a),find(b)
    # 이미 같은 집합에 있는 경우
    if a == b:
        return

    if rank[a] > rank[b]:
        # 이렇게 하면 항상 b가 랭크가 크게 된다.
        a,b = b,a
    nodes[a] = b

    if rank[a] == rank[b]:
        rank[b] += 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    nodes = [i for i in range(N + 1)]
    rank = [i for i in range(N + 1)]
    for i in range(M):
        oper,a,b = map(int,input().split())

        if oper == 0:
            # Union
            merge(a,b)

        else:
            # find
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
