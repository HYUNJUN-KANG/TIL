
# N, M
N, M = map(int, input().split())

# N * M 입력자료

arr = [list(map(int, input().split())) for _ in range(N)]

# arr = []
# for _ in range(N):
#     arr.append((list(map(int, input().split()))))

# 모든 사각영역의 좌상단 좌표
for x in range(0, N - M + 1):       # N-M 까지 될 수 있음. -> +1
    for y in range(0, N - M + 1):

        # (x,y)이고 크기가 M인 사각영역을 처리
        S = 0
        for i in range(x, x + M):
            for y in range(y, y+M):
                S += arr[i][j]
