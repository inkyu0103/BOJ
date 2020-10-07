#10799-1

user_input = input()

stick = 0
total_stick = 0

for i in range(len(user_input)):
    #스틱일 수도 있고, 레이저일 수도 있찌만...
    if user_input[i] == "(":
        stick += 1

    # 닫힌 경우 --> 레이저 or 막대기 끝
    else:
        stick -= 1
        #레이저인 경우
        if user_input[i-1] == "(":
            #스틱의 개수만큼 더한다
            total_stick += stick
        #막대기가 끝난 경우
        else:
            total_stick += 1

print(total_stick)






