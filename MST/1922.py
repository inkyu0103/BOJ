#1922 네트워크 연결
import sys

# find
def find(arr,x):
    if ds[x] != x:
        return find(arr,arr[x])
    return x

def union(arr,a,b):
    a = find(arr,a)
    b= find(arr,b)
    if a<b :
        arr[b] = a
    else:
        arr[a] = b

# 컴퓨터 수
cn = int(input())

# 집합
ds = [i for i in range(cn+1)]


# 연결 선 수
line = int(input())
edge = []

# 데이터 입력
for i in range(line):
    a,b,c = map(int,sys.stdin.readline().split())

    # 출발지와 도착지가 같은경우는 필요 없다.
    if a == b :
        continue
    # [비용 , [출발, 끝 ]]
    edge.append([c,[a,b]])

#정렬
edge.sort()
cost = 0

for e in edge :
    c,[a,b] = e
    # 부모가 다르면 Union (union은 수정해야할 듯)
    if find(ds,a) != find(ds,b):
        union(ds,a,b)
        cost += c

print(cost)
















