# 10816 숫자카드
'''
    카드의 개수에 대한 정보를 저장해놓는다. 배열에 해놓을까...? dic은 정렬이..
    dic에 개수 저장을 해야겠다. 그리고 이를 배열로 옮기도록 하자.

    그런 다음 이분 탐색으로 숑숑~
    시간초과 느낌 숑숑~
'''
import sys


input = sys.stdin.readline
def sol():
    num_dic = {}
    target = input()
    arr1= list(map(int,input().strip().split()))
    for i in arr1:
        if i not in num_dic:
            num_dic[i] = 1
        else:
            num_dic[i] += 1

    target = input()
    arr2= list(map(int,input().strip().split()))
    for i in arr2:
        if i in num_dic:
            print(num_dic[i], end=" ")
        else:
            print(0,end=" ")

sol()
