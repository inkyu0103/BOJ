#유기농 배추 시간초과

# 출처 https://m.post.naver.com/viewer/postView.nhn?volumeNo=27078300&memberNo=33264526

'''
    미리 방향을 다 설정하셨더라
    dirs [(1,0),(-1,0),(0,1),(0,-1)] --> 우,좌,상,하

    오... Map 과 Visited를 따로 만들어 줄 필요 없이 그냥 방문을 하면 0이라고 바꿔주시는 구나

    원래는 testCase = int(input()) 이런식으로 작성했는데,

    testCase = int(sys.stdin.readline()) 이게 좀 더 빠른 방법이다.

    그리고 지능형 리스트를 써서 좀 더 간결한 코드를 이용

    for j in range(N):
        Matrix.append([0]*M)
    -->

    maps = [[0 for _ in range(width)] for _ in range(height)] 오...

    생각보다 간단하게 구현할 수 있더라
'''
