# 17299 오등큰수
import sys

def sol():
    num = int(input())
    answer = [0]*num
    numArr = list(map(int,sys.stdin.readline().split()))
    numCountDic = {}
    # 이 부분에서 시간을 많이 잡아먹는 것 같으니 , 사전을 이용하자. -->이래도 시간 초과네;
    '''for i in range(len(numArr)):
        #있는 경우
        if numArr[i] in numCountDic:
            numCountArr[i] = numCountDic[numArr[i]]
        # 없는 경우
        else:
            numCountArr[i] = numArr.count(numArr[i])
            numCountArr[numArr[i]] = numCountArr[i]
    '''

    for i in numArr:
        try:
            numCountDic[i] += 1
        except:
            numCountDic[i] = 1

    stack = []

    for i in range(len(numArr)):
        # 최댓값이 아닌 경우
        # 스택이 빈 경우
        if not stack :
            stack.append((numCountDic[numArr[i]],i))

        # 마지막 값보다 지금 대상이 더 큰 경우
        elif stack[-1][0] < numCountDic[numArr[i]]:
            while(stack[-1][0] < numCountDic[numArr[i]]):
                val = stack.pop()
                answer[val[1]] = numArr[i]

                if not stack :
                    stack.append((numCountDic[numArr[i]],i))
                    break
            # 더 큰 아이 or 크기가 같은아이를 발견 하면 더해준다.
            stack.append((numCountDic[numArr[i]],i))

        # 마지막 값이 지금 대상보다 더 크거나 같은경우
        elif stack[-1][0] >= numCountDic[numArr[i]]:
            stack.append((numCountDic[numArr[i]],i))

    if stack:
        while(stack):
            val = stack.pop()
            answer[val[1]] = -1

    for i in answer:
        print(i,end=" ")
sol()
