# 1541 잃어버린 괄호

def sol(arr):
    mx = [[None for i in range(len(arr))] for j in range(len(arr)) ]
    mi = [[None for i in range(len(arr))] for j in range(len(arr)) ]
    def mxdp(a, b):
        if a == b:
            mx[a][b] = int(arr[a])
            mi[a][b] = int(arr[a])
        if mx[a][b] != None:
            return mx[a][b]

        tm = []
        for i in range(a+1,b,2):
            op = arr[i]
            if op == "+":
                tm.append(mxdp(a, i-1) + mxdp(i+1, b))
            elif op == "-":
                tm.append(mxdp(a, i-1) - midp(i+1, b))
        mx[a][b] = max(tm)
        return mx[a][b]

    def midp(a, b):
        if a == b:
            mx[a][b] = int(arr[a])
            mi[a][b] = int(arr[a])
        if mi[a][b] != None:
            return mi[a][b]

        tm = []
        for i in range(a+1,b,2):
            op = arr[i]
            if op == "+":
                tm.append(midp(a, i-1) + midp(i+1, b))
            elif op == "-":
                tm.append(midp(a, i-1) - mxdp(i+1, b))
        mi[a][b] = min(tm)
        return mi[a][b]
    return midp(0, len(arr)-1)



user_input = input()
process_input = []
tm = ""
for i in range(len(user_input)):

    if not user_input[i].isnumeric():
        process_input.append(tm)
        process_input.append(user_input[i])
        tm =""

    elif user_input[i].isnumeric():
        tm+=user_input[i]

process_input.append(tm)

print(sol(process_input))














