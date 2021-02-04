# 6549  히스토그램에서 가장 큰 사각형
import sys


def calc(arr):
    return min(arr)*len(arr)

def sol():
    while(1):
        data = list(map(int,sys.stdin.readline().split()))
        height = data[0]
        if not height:
            return

        else:
            graph = [[0]* height for i in range(height)]
            for i in range(1,height+1):
                graph[0][i-1] = data[i]


            for i in range(1,height):
                for j in range():
                    print(j,i+j+1)


sol()