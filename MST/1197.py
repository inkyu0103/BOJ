#최소 스패닝 트리

'''
    주의 : 가중치가 음수일 경우?
'''

def find(arr,n):
    if arr[n] == n:
        return n
    return find(arr,arr[n])

def simple_union(arr,a,b):
    a = find(arr,a)
    b= find(arr,b)
    if a<b :
        arr[b] = a
    else:
        arr[a] = b


import sys

V, E = map(int,input().split())
edge = []
weight = 0

#같은 집합인지 확인하기 위한 리스트
parents = [i for i in range(V+1)]

#정보 입력
for e in range(E):
    A,B,C = map(int,sys.stdin.readline().split())
    edge.append([C,(A,B)])

#가중치를 오름차순으로 정렬
edge.sort(key = lambda x: x[0])

for e in edge:
    w, start,end = e[0],e[1][0],e[1][1]

    # 두 노드의 root가 같으면 아무것도 x 이미 같은 집합
    if find(parents,start) != find(parents,end):
        simple_union(parents,start,end)
        weight += w

#정답 출력
print(weight)
