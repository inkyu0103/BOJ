# 1662 압축
# 메모리 초과
# 어떻게 해결하면 좋을까? 길이만 알면 되니까 실제로 문자를 더하고 곱할 필요는 없지 않을까?
# 메모리 초과가 나는 경우는 실제로 행위를 하지 않아도 될 수 있도록 정보를 같이 넣자.

# 1662 압축

def sol():
    string = input()
    totalLength = 0
    tmp = 0
    stack=[]
    for i in range(len(string)):
        if string[i].isdigit():
            totalLength += 1
            tmp = string[i]
        elif string[i] == "(":
            stack.append((tmp,totalLength-1))
            totalLength = 0
        elif string[i] ==")":
            multi,beforeLength=stack.pop()
            totalLength = (int(multi)*totalLength)+beforeLength
    print(totalLength)

sol()

