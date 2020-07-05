#1065

user_input = int(input())
count = 0
flag = 0

for j in range(1,user_input+1):
    flag = 0
    box = []
    for i in str(j):
        box.append(int(i))

    box_length = len(box)


    # 한 자리 수 또는 두 자리 수는 무조건 등차수열을 이룬다.
    if len(box) == 1:
        count+=1

    elif len(box) == 2:
        count += 1

    else:
        for k in range(box_length-2):
            if (box[k+1]-box[k] == box[k+2]-box[k+1]):
                continue
            else:
                flag = 1
                break

        if flag == 0 :
            count += 1


print(count)