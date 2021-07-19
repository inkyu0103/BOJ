# 15805 트리나라 관광 가이드
import sys
input = sys.stdin.readline

'''
visit 배열과 같이 사용해보자.
보통 부모 -> 자식 순으로 방문을 할텐데
'''

def sol():
    N = int(input())
    order = list(map(int,input().split(" ")))
    max_node = max(order) + 1
    parent = [0] * max_node
    visit = [0] * max_node

    for i in range(N):
        if not visit[order[i]]:
            if i == 0:
                parent[order[i]] = -1
            else:
                parent[order[i]] = order[i-1]
            visit[order[i]] = 1

    print(max_node)
    print(*parent)

sol()
