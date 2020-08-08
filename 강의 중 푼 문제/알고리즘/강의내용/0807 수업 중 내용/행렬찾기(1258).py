import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for x in range(1, T+1):

    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(n)]
#위 행렬을 입력받아서
#위 행렬을 입력받아서 행렬에 포함되어 있는 submatrx 크기 계산하기.

n = 6
matrix = [list(map(int, input().split()) for _ in range(n))]

# 할 일
# matrix 순회하면서 0이 아닌 위치 찾기
# 가로, 세로 길이 구해서 저장
# 표시한 영역은 0으로 다 바꾸기
    area = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                # 가로, 세로 길이 구하기
                x = 0     # 가로 길이
                for k in range(j, n):
                    if matrix[i][k]:
                        x += 1      # 0이 아니면 +1 해줌
                    else:
                        break

                y = 0
                for k in range(i, n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break

                # 표시한 영역은 다 0으로 바꾸기
                for k in range(i, i+y):     #세로 길이
                    for l in range(j, j+x):    #가로 길이
                        matrix[k][l] = 0

                area.append((y, x, y*x))

# tuple (y, x, y*x,) tuple을 사용함으로써 길이와  넓이를 다 가져옴

print(area)



# for row in matrix:
#     print(*row)