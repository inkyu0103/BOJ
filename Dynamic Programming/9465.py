# 9465
tc = int(input())

for _ in range(tc):
    length = int(input())
    value =[]

    #그래프
    for i in range(2):
        value.append(list(map(int,input().split())))

    if length == 1:
        print(max(value[0][0],value[1][0]))
        continue


    value[0][1] += value[1][0]
    value[1][1] += value[0][0]

    for i in range(2,length):
        value[0][i] += max(value[1][i-1],value[1][i-2])
        value[1][i] += max(value[0][i-1],value[0][i-2])

    print(max(value[0][-1],value[1][-1]))


'''
runtime err: 길이가 1인 경우?

'''









