#10799 쇠막대기

user_input = input()

stick = 0
tmp_laser = 0
total_laser = 0
total_stick = 0

for i in range(len(user_input)) :
    # ( 가 들어오면 스틱이 하나 시작된다.
    if user_input[i] == "(":
        stick += 1

    # ) 가 들어오면 스틱이 끝나던지 레이저가 발사된다.
    else:
        stick -= 1

        #이전이 ( 이면 레이저 발사
        if user_input[i-1] == "(":
            tmp_laser += 1

        #이전이 ) 이면 막대기가 끝나는 경우
        else:

            if tmp_laser != 0 :
                total_stick += (tmp_laser+1)
                total_laser += tmp_laser
                tmp_laser = 0

            else:
                total_stick += (total_laser + 1)

print(total_stick)



