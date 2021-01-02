# 1080 행렬
import sys

def sol():
    row , col = map(int,sys.stdin.readline().split())
    MA ,MB,Mark= [],[],[]



    # 기존행렬
    for r in range(row):
        tmp = [int(i) for i in sys.stdin.readline().rstrip()]
        MA.append(tmp)

    # 바뀐 행렬
    for r in range(row):
        tmp = [int(i) for i in sys.stdin.readline().rstrip()]
        MB.append(tmp)

    if row < 3 or col < 3:
        if MA == MB :
            print(0)
        else:
            print(-1)
        return


    for r in range(row):
        tmp =[]
        for c in range(col):
            if MA[r][c] == MB[r][c] :
                tmp.append(False)
            else:
                tmp.append(True)

        Mark.append(tmp)


    count = 0

    for r in range(0,row-2):
        for c in range(0,col-2):
            # 바꾸는 과정
            if Mark[r][c] == True:
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if Mark[i][j] == True:
                            Mark[i][j] = False
                        else:
                            Mark[i][j] = True
            count += 1

            if c == col-3 :
                for x in range(c,c+3):
                    if Mark[r][x] == True:
                        print(-1)
                        return

            if r == row -3:
                for x in range(r,r+3):
                    if Mark[x][c] == True:
                        print(-1)
                        return

            # 나머지 2*2
            if c == col-3 and r == row-3:
                for y in range(r+1,r+3):
                    for x in range(c+1,c+3):
                        if Mark[y][x] == True:
                            print(-1)
                            return


    print(count)
sol()



