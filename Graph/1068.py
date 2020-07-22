# 1068 트리
import sys

def DFS_del(num):
    for i in range(num,len(tree)):
        if tree[i] == num:
            DFS_del(i)

    tree[num] = -100

def DFS_chc(num):
    for i in range(num,len(tree)):
        if tree[i] == num:
            #같은 애가 있으면 자식이 아니므로 count 추가 x
            return 0
    #같은아이가 없어!! 그럼 count 추가
    return 1

nodeNum = int(sys.stdin.readline())
tree = list(map(int,sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
count =0

DFS_del(delete)

for i in range(len(tree)-1,-1,-1):
    if tree[i] != -100:
        count += DFS_chc(i)
print(count)
