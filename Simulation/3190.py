# 3190 뱀
import sys

def sol ():
    #시간
    sec = 0
    # row . col 순으로  --  서 북 동 남
    dirs=[(0,-1),(-1,0),(0,1),(1,0)]
    inital_dir = 2


    head =[1,1]
    body = []

    board = int(sys.stdin.readline())
    appleNum = int(sys.stdin.readline())
    appleData = [list(map(int,sys.stdin.readline().split())) for _ in range(appleNum)]

    dirNum = int(sys.stdin.readline())
    dirData = []
    for i in range(dirNum):
        S,D = sys.stdin.readline().split()
        dirData.append((int(S),D))


    for i in dirData:
        print("지금 갱신된 초 수 :",  sec)
        print("HEAD : {} , BODY : {} ".format(head,body))
        S,D = i


        for j in range(1,S-sec+1):
            # 헤드가 벽이 아니면...
            if 0 < head[0] + dirs[inital_dir][0] < board+1 and 0 < head[1] + dirs[inital_dir][1] < board + 1:
                # 헤드 정보를 갱신
                head[0] += dirs[inital_dir][0]
                head[1] += dirs[inital_dir][1]

                # 만약 갱신했는데, 거기에 사과가 있다면? body에 추가
                if (head[0],head[1]) in appleData:
                    print("홀리몰리 사과가 있넹 옴뇸뇸", body)
                    body.append((head[0],head[1]))
                    appleData.remove((head[0],head[1]))

            # 헤드가 몸체 안에 있다면?
            elif (head[0] + dirs[inital_dir][0],head[1] + dirs[inital_dir][1]) in body:
                # 초를 가르쳐 주고 끝내자.
                print("{} 초에서 BITE ME ;ㅁ;".format(sec+j))
                return sec + j

            # 그 이외 모든 경우...?라고 해도 될지...
            else:
                print("{} 초에서 콰당".format(sec+j))
                return sec + j

        # 방향도 갱신
        if D == "L":
            inital_dir -= 1
            if inital_dir < 0:
                inital_dir = 3

        elif D == "D":
            inital_dir += 1
            if inital_dir > 3:
                inital_dir = 0
    #시간을 한번에 갱신해야 할지...
        sec = S

    # 어라 방향 전환때 안 부딪혔니?
    while(1):
        #계속 그 방향으로 가자~
        if 0 < head[0] + dirs[inital_dir][0] < board + 1 and 0 < head[1] + dirs[inital_dir][1] < board + 1:
            # 헤드 정보를 갱신
            head[0] += dirs[inital_dir][0]
            head[1] += dirs[inital_dir][1]

            sec += 1
        else:
            break

    print(sec)
    return sec


print(sol())

