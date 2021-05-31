# 6549  히스토그램에서 가장 큰 사각형
import sys
input = sys.stdin.readline

def sol():
    while(1):
        N,*arr = list(map(int,input().split()))
        if N == 0:
            return
        left = [0] * (N)
        right = [0] * (N)
        stack = [(0,-1)]
        answer_group = []

        for i in range(N):
            if arr[i] > stack[-1][0]:
                left[i] = stack[-1][1]
                stack.append((arr[i],i))

            elif arr[i] <= stack[-1][0]:
                right[stack[-1][1]] = i
                while(stack and arr[i] <= stack[-1][0]):
                    val = stack.pop()
                    right[val[1]] = i
                left[i] = stack[-1][1]
                stack.append((arr[i],i))

            if i==N-1:
                val = stack.pop()
                right[i] = val[1]+1


        for i in range(1,N):
            answer_group.append((right[i]-left[i]-1)* arr[i])
        print(max(answer_group))
sol()