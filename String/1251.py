# 1251
from itertools import combinations
import sys
input = sys.stdin.readline

def sol():
    target = input().rstrip()
    length = len(target)
    result =[]

    #아하 각 부분이 한 개 이상의 문자를 가지고 있어야 한다.
    for candidate in combinations(range(length),2):
        first,second= candidate

        if second != length-1:
            first_reverse = target[:first+1][::-1]
            second_reverse = target[first+1:second+1][::-1]
            third_reverse = target[second+1:][::-1]

            result.append(first_reverse+second_reverse+third_reverse)

    #heap을 써도 되려나?
    result.sort()

    print(result[0])


sol()