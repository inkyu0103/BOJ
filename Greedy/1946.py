# 신입사원

import sys
tc = int(input())



for i in range(tc):
    data = []
    num = 1
    uc = int(sys.stdin.readline())
    for j in range(uc):
        data.append(list(map(int,sys.stdin.readline().split())))

    # 첫 번째 항목 기준 정렬
    data.sort(key = lambda x:x[0])
    # 제일 낮은 기준점
    mi = data[0][1]

    for i in range(1,len(data)):
        if data[i][1] < mi :
            mi = data[i][1]
            num +=1


    print(num)
