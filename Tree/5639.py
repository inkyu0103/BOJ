# 5639 이진 검색 트리
'''
    전위 순회를 줄테니 후위순회를 내놓아
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def divide(start,end):

    if start > end :
        return

    if start == end :
        print(preorder[start])
        return

    root = preorder[start]
    larger_idx = -1
    for i in range(start,end+1):
        if preorder[i] > root:
            larger_idx = i
            break

    # larger_idx가 -1인 경우에는 더 큰 값이 발견이 되지 않았으므로 왼쪽만 있는 경우이다.
    # 우편향 , 좌편향 트리.

    # 오른쪽에 더 큰 아이가 없는 경우
    if larger_idx == -1:
        divide(start+1,end)

    else:
        divide(start+1,larger_idx-1)
        divide(larger_idx,end)

    print(root)



if __name__ == "__main__":
    preorder = []
    while True:
        node = input().strip()

        if len(node) == 0:
            break

        preorder.append(int(node))

    divide(0,len(preorder)-1)