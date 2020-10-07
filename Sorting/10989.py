# 수 정렬하기 3
# EOF 문제   --> try ~ except로 해결
# 파라미터로 넣는 경우와 그렇지 않은 경우의 차이가 있을까?

import sys

def countSorting(arr):
    max_length = 10000
    C = [0]*1
    B = [0]*(max_length+1)

    for i in range(length):
        C[arr[i]] += 1

    #누적 배열
    for i in range(1,length):
        C[i] += C[i-1]

    for i in range(length-1,-1,-1):
        B[C[arr[i]]] = arr[i]
        C[arr[i]] -= 1

    return B


num = int(input())
numbers = []

for i in range(num):
    numbers.append(int(input()))

a= countSorting(numbers)
for i in range(1,len(a)):
    print(a[i])



