T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        cnt = 0

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[i][j] += color
                
            if color == 3:
                cnt += 1
                # if arr[i][j] == 0:
                #     arr[i][j] = color
                # else:
                #     arr[i][j] = 3
                # arr[i][j] = color


    for lst in arr:
        print(*lst)  # @@@@   *붙이면 [] 없어짐

