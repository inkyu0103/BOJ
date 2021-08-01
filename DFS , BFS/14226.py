# 14226 이모티콘 (시작 시간 1시 11분 1차 제출 1시 34분 : 23분 소요 - 메모리 초과)
'''
화면에 있는 아이를 기준으로 해야겠네?
클립 보드에 있는 아이가 문제.
0이 되는건 아예 막아야겠다.
중복되는 경우가 많음
'''
# time, clip_board,display_emo
def bfs():
    display_emoticon = 1
    q = deque([(0,0,display_emoticon)])
    visit = set()
    visit.add((0,0,display_emoticon))


    while q:
        cur_time,cur_clip,cur_emo = q.popleft()
        if cur_emo == N:
            print(cur_time)
            return

        # 클립보드에 복사하는 경우 ( cur_emo가 있는 경우 )
        target = (cur_time + 1, cur_emo, cur_emo)
        if cur_emo and target not in visit:
            q.append(target)
            visit.add(target)

        # 클립보드에서 cur_emo로 복사하는 경우
        if cur_clip :
            target = (cur_time+1,cur_clip,cur_clip+cur_emo)
            if target not in visit:
                q.append(target)
                visit.add(target)

        # 한개 제거하는 경우
        if cur_emo > 1 :
            target = (cur_time+1,cur_clip,cur_emo-1)
            if target not in visit:
                q.append(target)
                visit.add(target)



from collections import deque
import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    bfs()
