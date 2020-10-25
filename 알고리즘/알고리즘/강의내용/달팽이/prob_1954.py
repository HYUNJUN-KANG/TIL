import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    B = int(input())
    B_list = []


    for i in range(1, B*B+1):
        B_list.append(i)

    list_B = []

    for j in range(1, tc):


        for k in range(1, tc+1):
            tmp = []
            for q in range(1 + tc*(k-1), (k * tc) + 1):
                tmp.append(q)
            list_B.append(tmp)
    print(list_B)

    cnt = tc * tc             # 채워줄 숫자
    # deltas : 우 하 좌 상                 B/C 달팽이 순회 순서
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    x = 0  # 가로 좌표
    y = 0  # 세로 좌표
    d = 0  # 델타 인덱스
    num = 1 # 증가하는 숫자 (배열을 채울 숫자)

    while num <= cnt:      # 총 tc * tc 개의 숫자를 채워야함

        # 벽 이거나, 채울 수 없으면 방향 전환

        if 0 <= x < tc and 0 <= y < tc and not arr[x][y]:             # 시작점이 [0,0] 일때만 출발하라.
            arr[x][y] = num
            num += 1

        else:      # 범위를 벗어남
            x -= dx[d]
            y -= dy[d]
            d = (d + 1) % 4                     # 4 이내에서 수가 반복해야 하므로 % 4

        x += dx[d]
        y += dy[d]

    for row  in arr:
        print(row)

