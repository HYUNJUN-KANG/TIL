import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0  # 단어가 들어갈 수 있는 개수를 세기 위한 변수

    # 행 조사
    for i in range(N):
        length = 0
        for j in range(N):
            if board[i][j] == 1:
                length += 1  # 1이 나오면 길이 +1
            else:  # 0이 나오면, 길이 검사 후 길이를 0으로 만듦.
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    # 열 조사
    for j in range(N):
        length = 0
        for i in range(N):
            if board[i][j] == 1:
                length += 1  # 1이 나오면 길이 +1
            else:  # 0이 나오면, 길이 검사 후 길이를 0으로 만듦.
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))