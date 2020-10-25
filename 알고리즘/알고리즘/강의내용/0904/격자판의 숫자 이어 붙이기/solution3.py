def dfs(r, c, cnt, number):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # r,c는 현재좌표
    # cnt 현재까지 연결한 숫자 개수
    # number 현재까지 연결된 중간결과

    if cnt == 6:    # 숫자 7개를 모두 만들었으면, 더이상 재귀호출 x
        result.add(number)
        return

    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            new_number = number + board[nr][nc]
            dfs(nr, nc, cnt+1, new_number)

T = int(input())

for tc in range(1, T+1):
    N = 4
    board = [list(input().split()) for _ in range(N)]
    result = set()
    # 모든 칸이 시작점이 될 수 있음을 고려
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, board[i][j])

    print('#{} {}'.format(tc, len(result)))