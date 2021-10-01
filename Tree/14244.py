# 14244
'''
ex) 4 2
하나는 루트 ,
노드 3개 리프 2개
따라서 리프 2개는 따로 달고

    N-1-L

'''
import sys
input = sys.stdin.readline

def sol():
    N,L = map(int,input().split())
    node = [0] * (N)

    node[0] = 1
    successive=N-1-L

    for i in range(2,2+successive):
        node[i] = i-1

    for i in range(2+successive,N):
        node[i] = 0

    for idx,val in enumerate(node):
        print(idx, val)

sol()