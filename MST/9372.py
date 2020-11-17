# 9372 상근이의 여행
import sys

def find_parent(a,b,arr):
    a_val = a
    b_val = b

    # find root
    while(1):
        if arr[a_val] != a_val:
            a_val = arr[a_val]
        else:
            break
    while(1):
        if arr[b_val] != b_val:
            b_val = arr[b_val]
        else:
            break

    if a_val == b_val:
        return True
    else:
        return False




tc = int(input())
for i in range(tc):
    city,airplane =  map(int,input().split())
    answer = 0
    # 0 ~ the num of city
    joint = [i for i in range(city+1)]
    print(joint)
    edge  = []

    #정보 입력
    for j in range(airplane):
        edge.append(list(map(int,sys.stdin.readline().split())))

    for k in edge :
        a,b = k[0],k[1]
        value = find_parent(a,b,joint)

        # 두 집합이 다르다면 , 간선 추가
        if not value:
            answer += 1
            joint[min(a,b)] = max(a,b)

    print(answer)










