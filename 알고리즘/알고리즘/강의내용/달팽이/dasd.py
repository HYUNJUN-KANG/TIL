import sys
sys.stdin = open('input.txt', 'r')

def delta(n):
    cnt = arr[0][0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]  # 우하좌상
    xx = yy = 0
    d = 0
    while cnt != (n ** 2):
        new_x = xx + dx[d]
        new_y = yy + dy[d]
        if 0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y] == 0:
            cnt += 1
            arr[new_x][new_y] = cnt
            xx = new_x
            yy = new_y
        else:
            d = (d + 1) % 4


for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    delta(N)
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
