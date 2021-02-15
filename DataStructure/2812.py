# 2812

def sol():
    # N개중 K개를 빼는 것. 따라서  COUNT가 K가 되면 더 이상 빠지는 것 없이 추가.
    N,K = map(int,input().split())
    user_input = input()
    stack =[]
    count = 0

    for i in user_input:
        # 스택이 비었다면?
        if len(stack) == 0:
            stack.append(i)

        # 스택의 마지막이 현재 대상보다 작거나 같다면?
        elif int(stack[-1]) < int(i):
            while stack and int(stack[-1]) < int(i) and count != K:
                stack.pop()
                count += 1
            stack.append(i)



        # 스택의 마지막이 더 큰 경우
        elif int(stack[-1]) >= int(i):
            stack.append(i)

        '''
            근데 이럴 때 문제는 98765 (5,2) 이렇게 되면 뺄 대상이 없다는 것임. 그냥 계속 추가만 하게됨.
            그럼 맨 마지막에 count가 도달하지 않으면 그 개수만큼 빼주면 되려나?
        '''

    if count != K:
        while(count != K):
            stack.pop()
            count += 1


    print("".join(stack))
sol()

