x = 1
y = 1

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]


for i in range(8):

    nx = x + dx[i]
    ny = y + dy[i]
    new = arr[nx][ny]
    print(new)