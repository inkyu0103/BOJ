#1439 뒤집기
def sol () :
    string = input()

    zero = 0
    one  = 0

    for i in range(len(string)-1):
        # 1일때 바꾸자
        if string[i] == '1':
            if string[i+1] == '0': # 이전항목과 다르면 추가.
                one += 1
            else:
                continue

    if string[len(string)-1] == '1':
        one += 1




    for i in range(len(string) - 1):
        if string[i] == '0':
            if string[i + 1] == '1':
                zero += 1
            else:
                continue

    if string[len(string)-1] == '0':
        zero += 1

    # 아 맨 마지마지막에서 이렇게 짜면 다른 경우에만 '10' 더하겠구나, 같은경우에도 마지막에는 1더해줘야한다.

    print(one,zero)
    return ;

sol()