import math





def solution(arr):
    maxi = [[None for i in range(len(arr))] for j in range(len(arr))]
    mini = [[None for i in range(len(arr))] for j in range(len(arr))]

    def mxdp(x,y):
        if x==y:
            maxi[x][y] = int(arr[x])
            mini[x][y] = int(arr[x])

        if maxi[x][y] !=None:
            return maxi[x][y]

        tmp=[]

        for i in range(x+1,y,2):
            operator = arr[i]
            if operator == "+":
                tmp.append(mxdp(x,i-1)+mxdp(i+1,y))
            elif operator == "-":
                tmp.append(mxdp(x,i-1)-midp(i+1,y))

        maxi[x][y] = max(tmp)
        return maxi[x][y]

    def midp(x, y):
        if x == y:
            maxi[x][y] = int(arr[x])
            mini[x][y] = int(arr[x])

        if mini[x][y] != None:
            return mini[x][y]

        tmp = []

        for i in range(x + 1, y, 2):
            operator = arr[i]
            if operator == "+":
                tmp.append(midp(x, i - 1) + mxdp(i + 1, y))
            elif operator == "-":
                tmp.append(midp(x, i - 1) - mxdp(i + 1, y))

        mini[x][y] = min(tmp)
        return mini[x][y]


    return mxdp(0,len(arr)-1)






