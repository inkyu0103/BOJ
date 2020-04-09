#2231 분해합

user_input = int(input())
flag = 0 # 다 돌았을 때 없으면 플래그가 0

#아마 자리수 * 9 범위 내부터 돌면 될 듯 싶은데
input_string_num =len(str(user_input))
if user_input - input_string_num * 9 < 0:
    val = 0
else :
    val = user_input-input_string_num*9

for i in range(val,user_input):


    result = 0
    for j in str(i):
        result += int(j)
    result += i

    if result == user_input :
        print(i)
        flag = 1
        break;

if flag == 0 :
    print (0)

