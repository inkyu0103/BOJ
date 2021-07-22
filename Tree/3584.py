# 3584 가장 가까운 공통 조상
# 분리집합? 근데 시간복잡도가 될까? 일단 해보기나 합시다
# 자기 자신이 공통조상일 수도 있구나.

import sys
input = sys.stdin.readline



def LCA(node1,node2):
    parent1 = []
    parent2 = []
    print(node1,node2)
    while 1:
        node1_p = parent[node1]
        parent1.append(node1_p)

        if node1_p == parent[node1_p]:
            break

        node1 = node1_p

    while 1:
        node2_p = parent[node2]
        parent2.append(node2_p)

        if node2_p == parent[node2_p]:
            break

        node2 = node2_p


    print(parent1,parent2)






if __name__ =='__main__':
    tc = int(input())
    for _ in range(tc):
        node = int(input())
        parent = [i for i in range(0,node+1)]

        for e in range(node-1):
            p,c = map(int,input().split())
            parent[c] = p

        n1,n2 = map(int,input().split())
        LCA(n1,n2)



