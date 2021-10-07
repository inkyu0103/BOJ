# 20437

import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
MINF = -1

def sol():
    tc = int(input())

    for _ in range(tc):
        min_dict = defaultdict(lambda :INF)
        max_dict = defaultdict(lambda :-1)

        string = input().rstrip()
        K = int(input())
        length = len(string)

        for char in string:
            min_dict[char]
            max_dict[char]

        for i in range(length-1):
            count = 1
            for j in range(i+1,length):
                if string[i] == string[j]:
                    count += 1

                if count == K:
                    min_dict[string[i]] = min(min_dict[string[i]],j-i+1)
                    max_dict[string[i]] = max(max_dict[string[i]],j-i+1)
                    break


        min_result = sorted(list(min_dict.items()),key=lambda x:x[1])
        max_result = sorted(list(max_dict.items()),key=lambda x:-x[1])

        if min_result[0][1] == INF or max_result[0][1] == MINF:
            print(-1)

        else:
            print(min_result[0][1], max_result[0][1])

def sol2():
    tc = int(input())

    for _ in range(tc):
        idx_info = defaultdict(list)
        string = input().strip()
        k = int(input())

        for idx,char in enumerate(string):
            idx_info[char].append(idx)

        min_length = INF
        max_length = MINF

        for key in idx_info:
            length = len(idx_info[key])

            if length< k:
                continue

            else:
                for i in range(length-k+1):
                    min_length = min(idx_info[key][i+k-1]-idx_info[key][i]+1,min_length)
                    max_length = max(idx_info[key][i+k-1]-idx_info[key][i]+1,max_length)

        if min_length == INF or max_length == MINF:
            print(-1)
        else:
            print(min_length,max_length)

sol2()









