#1085 직사각형에서 탈출

x,y,w,h = map(int,input().split())

#현 위치 (x,y) 오른쪽 꼭짓점 (w,h)
print(min(x,y,w-x,h-y))



