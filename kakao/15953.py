case = int(input())

x = [0,5000000,3000000,2000000,500000,300000,100000]
y = [0,5120000,2560000,1280000,640000,320000]

for i in range(case):
    answer = 0
    a,b = map(int,input().split())

    if a == 1:
        answer += x[1]
    elif 2<=a<=3 :
        answer += x[2]
    elif 4<=a<=6:
        answer += x[3]
    elif 7<=a<=10:
        answer += x[4]
    elif 11<=a<=15:
        answer += x[5]
    elif 16<=a<=21 :
        answer += x[6]

    if b == 1:
        answer += y[1]
    elif 2<=b<=3:
        answer += y[2]
    elif 4<=b<=7 :
        answer  += y[3]
    elif 8<=b<=15:
        answer += y[4]
    elif 16<=b<=31:
        answer += y[5]

    print(answer)