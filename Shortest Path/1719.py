# 1719 택배

import sys
input = sys.stdin.readline
INF = sys.maxsize

def Floyd(n):
    for k in range(n):
        for s in range(n):
            for e in range(n):
                if adj_matrix_time[s][e] > adj_matrix_time[s][k] + adj_matrix_time[k][e]:
                    adj_matrix_time[s][e] = adj_matrix_time[s][k] + adj_matrix_time[k][e]
                    answer[s][e] = answer[s][k]

if __name__ == '__main__':
    n,m = map(int,input().split())
    adj_matrix_time = [[INF]*n for _ in range(n)]
    answer = [[0]*n for _ in range(n)]

    for i in range(n):
        answer[i][i] = "-"
        adj_matrix_time[i][i] = 0

    for _ in range(m):
        s,e,time = map(int,input().split())

        # 양방향 그래프
        adj_matrix_time[s-1][e-1] = time
        adj_matrix_time[e-1][s-1] = time

        answer[s-1][e-1] = e
        answer[e-1][s-1] = s

    Floyd(n)

    for i in answer:
        print(*i)