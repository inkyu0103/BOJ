# 14675 단절점과 단절선
# 입출력이 귀찮네요... 어떻게 하는지 지켜봅시다.
# 트리가 주어지므로 아무 노드에서나 시작해도 된다.
# 문제를 잘 읽으쇼...
# 트리라는 특성때문에 사이클 자체가 없으니까 단절점이라고 판단되는 아이들의 자식만 보면 된다.
# 뭔 뻘짓을 한겨...

'''
결론 :
한 정점에서 연결된 아이가 2개 이상이면 걍 단절점이다.왜? 트리니까
'''

import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    N = int(input())
    tree = [[] for _ in range(N+1)]
    edges = []

    for _ in range(N-1):
        s,e = map(int,input().split())
        edges.append((s,e))
        tree[s].append(e)
        tree[e].append(s)

    Q = int(input())
    for _ in range(Q):
        c,target = map(int,input().split())

        # 단절점 찾는 경우
        if c == 1:
            if len(tree[target]) == 1:
                print("no")
            else:
                print("yes")

        # 아니 모두 단절선이잖어
        else:
            print("yes")
