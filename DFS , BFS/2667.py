# 2667 단지번호 붙이기





# complex : 단지 수
# count : 단지 내 아파트 개수

Vertex = int(input())

Matrix = []
Visit = []
Stack = []

count = 0
complex = 0
complex_num = []

for i in range(Vertex):
    Visit.append([0] * Vertex)
    tmp = []
    for i in input():
        tmp.append(int(i))

    Matrix.append(tmp)

print(Matrix)
print(Visit)


while(1):

    count = 0

    Find()

    val = find_start()

    if val == False:
        break
    else:
        continue


print("Complex : " , complex)
print("Complex Num : ", complex_num)
#방문 결과는 잘 나온다.
print(Visit)