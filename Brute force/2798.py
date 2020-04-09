import math
# 블랙 잭

card_num , sum_expect = map(int, input().split())
card_box = list(map(int, input().split()))
# diff = 값의 차 , Max = 그 때의 sum
diff = math.inf
Max = 0
flag = 0

# sum_expect - real_sum 이 가장 작은 것을 뽑자. 단, sum_expect < real_sum인 경우에는 그냥 지나친다.
for i in range(card_num-2):
    for j in range(i+1,card_num-1):
        for k in range (i+2,card_num):
            real_sum = card_box[i]+card_box[j]+card_box[k]
            if (sum_expect < real_sum):
                continue
            elif (sum_expect == real_sum):
                flag = 1
                break  # 이 break;문의 범위가 어디일런지... for k 부분이려나? 확인해봐야 하네.
            else:
                # 처음에 diff =0 으로 잡게 되면 계산 1도 못함 ㅋ  --> math.inf
                if (sum_expect - real_sum < diff):
                    #새로운 diff,real_sum 설정
                    diff = sum_expect-real_sum
                    Max = real_sum


        if (flag ==1):
            break;
    if(flag == 1):
        break;

if flag == 1 :
    print(sum_expect)

else :
    print(Max)


