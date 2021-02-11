# 2812

def sol():
    N,K = map(int,input().split())
    user_input = input()
    stack =[]
    count = 0

    for i in range(len(user_input)):
        # 스택이 빈 경우에는 추가
        if count == K:
            stack.append(user_input[i])

        else:
            if len(stack) == 0 :
                stack.append(user_input[i])

            # 스택의 마지막이 현재 대상보다 작거나 작은 경우
            elif int(stack[-1]) > int(user_input[i]):
                stack.append(user_input[i])

            # 스택의 마지막이 현재 대상보다 큰 경우 --> else 처리하면 어떻게 되지
            elif int(stack[-1]) <= int(user_input[i]):
                while(1):
                    stack.pop()
                    count += 1
                    # 이 부분을 고려 못했네;
                    if len(stack) == 0:
                        stack.append(user_input[i])
                        break

                    elif int(stack[-1]) > int(user_input[i]):
                        stack.append(user_input[i])
                        break

                    elif count == K :
                        stack.append(user_input[i])
                        break



    print("".join(stack))


sol()

