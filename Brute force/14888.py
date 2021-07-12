import sys
from itertools import permutations
from collections import deque
import copy

input = sys.stdin.readline
INF = sys.maxsize

def sol():
    N = int(input())
    oper_arr = []
    max_val , min_val = -INF,INF
    num_list = input().strip().split(" ")
    p,s,m,d = map(int,input().split())
    oper_arr += ["+"]*p + ["-"]*s + ["*"]*m + ["//"]*d



    for exp in set(permutations(oper_arr)):
        q = deque(exp)
        num_list_iter = 1
        result = int(num_list[0])

        while(q):
            operation = q.popleft()
            if operation == "+":
                result += int(num_list[num_list_iter])
            elif operation == "-":
                result -= int(num_list[num_list_iter])
            elif operation == "*":
                result *= int(num_list[num_list_iter])
            else:
                if result < 0:
                    result = -result
                    result //= int(num_list[num_list_iter])
                    result = -result
                else:
                    result //= int(num_list[num_list_iter])

            num_list_iter += 1


        max_val = max(max_val , result)
        min_val = min(min_val , result)


    print(max_val)
    print(min_val)


sol()
