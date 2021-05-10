#5397
import sys
from collections import deque
input = sys.stdin.readline

def sol():
    a = int(input())
    for i in range(a):
        password = input().strip()
        q = []
        word = []

        for c in password:
            if c =="<" and word:
                q.append(word.pop())

            elif c==">" and q :
                word.append(q.pop())

            elif c=="-" and word:
                word.pop()

            elif c not in "<>-":
                word.append(c)

        print("".join(word) + "".join(q)[::-1])
sol()
