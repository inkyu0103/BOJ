# 20001 고무오리 디버깅
import sys
input = sys.stdin.readline

def sol():
    start = input()
    stack = []
    while(1):
        q = input().strip()
        if q == "문제":
            stack.append("문제")

        elif stack and q =="고무오리":
            stack.pop()
        elif not stack and q=="고무오리":
            stack.append("문제")
            stack.append("문제")
        elif q == "고무오리 디버깅 끝":
            break

    if stack:
        print("힝구")
    else:
        print("고무오리야 사랑해")

sol()
