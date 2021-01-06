# 1744 수 묶기

import sys


# 케이스를 잘 나눠서 생각하자
def sol():
    case = int(sys.stdin.readline())
    num_list = [int(sys.stdin.readline()) for i in range(case)]
    answer = 0

    pos=[]
    neg=[]

    for i in num_list:
        if i <= 0 :
            neg.append(i)
        elif i == 1:
            answer += 1

        else :
            pos.append(i)

    pos.sort(reverse=True)
    neg.sort()

    for i in range(0,len(neg),2):
        if i+1 < len(neg):
            answer += neg[i]*neg[i+1]
        else:
            answer += neg[i]

    for i in range(0,len(pos),2):
        if i+1 < len(pos):
            answer += pos[i]*pos[i+1]
        else:
            answer += pos[i]

    print(answer)


sol()

