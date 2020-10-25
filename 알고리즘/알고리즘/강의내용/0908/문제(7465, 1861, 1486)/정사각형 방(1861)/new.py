import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    cnt = 0
    stack = list()
    stack.append((r, c))

    while stack:
        cr, cc = stack.pop()
        cnt += 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[cr][cc] + 1:
                stack.append((nr, nc))
                break

        else:
            return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(rooms)

    # 가장 많은 개수의 방을 이동
    max_cnt = 0

    # 가장 많은 개수의 방을 이동할 수 있는 시작하는 방의 번호
    start_room_number = (N * N + 1)

    # 시작점 탐색
    for r in range(N):
        for c in range(N):
            room_number = rooms[r][c]
            cnt = dfs(r, c)
            if cnt > max_cnt:
                max_cnt = cnt
                start_room_number = room_number
            elif cnt == max_cnt:
                if room_number < start_room_number:
                    start_room_number = room_number

    print("#{} {} {}".format(tc, start_room_number, max_cnt))