# 행렬 곱셈 순서

num_of_matrix = int(input())
matrix_info = []
INF = 10e20

#matrix info
for i in range(num_of_matrix):
    row,col = map(int,input().split())
    if i == 0 :
        matrix_info.append(row)
        matrix_info.append(col)

    else:
        matrix_info.append(col)

# dp
if num_of_matrix == 3:
    print(matrix_info[0]*matrix_info[1]*matrix_info[2])

else:
    dp = [[0]*(num_of_matrix+1) for i in range(num_of_matrix+1)]
    print(dp)
    for l in range(2,num_of_matrix+1):
        for i in range(1,num_of_matrix-l+2):
            j = i+l-1

            dp[i][j] = INF
            for k in range(i,j):
                q = dp[i][k] + dp[k+1][j] + matrix_info[i-1]*matrix_info[k]*matrix_info[j]

                if q<dp[i][j] :
                    dp[i][j] = q

    print(dp)

