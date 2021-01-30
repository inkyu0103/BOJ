# 2493 탑

towerNum = int(input())
height = list(map(int,input().split()))
answer = [0]*towerNum
stack = []

for i in range(towerNum):
    if i == 0:
        stack.append((height[0],i))

    else:
        # 자기보다 낮은 아이가 발견되면 뺴준다.
        while(stack and stack[-1][0] < height[i]):
            stack.pop()
        if stack:
            answer[i] = stack[-1][1]+1

        stack.append((height[i],i))

print(' '.join(map(str,answer)))







