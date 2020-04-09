#7568

test_case = int(input())
data = []
for i in range(test_case):
    W ,L = map(int,input().split())
    data.append([W,L,1])


for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            data[i][2] += 1
            continue
        elif ((data[i][0]>data[j][0] and data[i][1]<data[j][1])):
            continue;
        elif ((data[i][0]<data[j][0] and data[i][1]>data[j][1])):
            continue;
        elif data[i][0]>data[j][0] and data[i][1]>data[j][1]:
            data[j][2] +=1
            continue


for i in range(len(data)):
    print(data[i][2],end=' ')



