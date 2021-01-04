# 1138 한 줄로 서기
import sys

def sol():
    num = int(input())
    height_info = list(map(int,sys.stdin.readline().split()))
    answer = []


    for i in range(num-1,-1,-1):
        answer.insert(height_info[i],i+1)

    for a in answer :
        print(a,end=" ")


sol()






