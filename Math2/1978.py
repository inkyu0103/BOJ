import math

test_case  = int(input())
user_data = list(map(int,input().split()))
data = [i for i in range(3,int(math.sqrt(1000)+3),2)]
counter =0
if test_case == (len(user_data)):
    for i in user_data:
        flag = 0
        btn = True

        if i == 1 :
            continue
        elif i == 2 :
            counter += 1
            continue
        #이미 2를 제외한 짝수는 다 거름
        elif i != 2 and i%2 == 0:
            continue

        else :
            for check in data :
                #오 check가 열심히 돌았는데, i보다 커졌네
                if check >= i :
                    btn =True
                    break;

                elif check < i :
                    if i%check == 0:
                        break
            #모두 검사했을 때 나누지지 않는 수
            if btn  == True :
                flag = 1
        if flag == 1:
            counter+=1
    print(counter)