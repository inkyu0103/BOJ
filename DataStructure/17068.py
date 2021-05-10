# 17068 막대기

import sys
input = sys.stdin.readline

def sol():
    num = int(input())
    box = [int(input()) for _ in range(num)]
    target = box[-1]
    answer = 1

    for i in range(num-1,-1,-1):
        if box[i] > target:
            target = box[i]
            answer += 1

    print(answer)

sol()
