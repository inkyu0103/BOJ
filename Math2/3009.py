#3009 네 번째 점
x_stack=[]
y_stack=[]

for i in range(3):
    x,y = map(int,input().split())
    if x not in x_stack:
        x_stack.append(x)
        if y not in y_stack:
            y_stack.append(y)
        else:
            y_stack.remove(y)

    else:
        x_stack.remove(x)
        if y not in y_stack:
            y_stack.append(y)
        else:
            y_stack.remove(y)

print(x_stack[0],y_stack[0])

