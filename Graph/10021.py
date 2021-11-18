# 10021
from collections import deque,defaultdict
import sys
input = sys.stdin.readline


def cal_dist(node1,node2):
    return (node1[0]-node2[0])**2 + (node1[1]-node2[1])**2

def sol():
    N,C = map(int,input().split())
    Nodes = defaultdict(list)
    visit = set()

    edge_costs = []

    # 노드 정보 입력하기.
    for i in range(N):
        Nodes[i+1] = list(map(int,input().split()))

    for i in range(1,N):
        for j in range(i+1,N+1):
            # 노드간 거리, 시작노드 끝 노드
            edge_costs.append([cal_dist(Nodes[i],Nodes[j]), i,j])

    edge_costs.sort(key=lambda x:x[0])
    count = 0
    total_cost = 0
    break_flag = 0

    for cost,start,end in edge_costs:
        flag = 0
        if cost >= C :
            if start not in visit:
                visit.add(start)
                flag = 1

            if end not in visit:
                visit.add(end)
                flag = 1

        if flag:
            total_cost += cost
            count += 1

        if count == N-1:

            break_flag = 1
            break

    print(total_cost if break_flag else -1)

sol()