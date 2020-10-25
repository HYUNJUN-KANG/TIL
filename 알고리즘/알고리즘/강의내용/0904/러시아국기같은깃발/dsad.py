import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def comb(li, idx, cnt):
    global new_li
    global real_li
    if cnt == T:
        if new_li[1] != N - 1:
            real_li += new_li
        return
    if idx >= N:
        return

    new_li.append(idx)
    comb(new_li, idx + 1, cnt + 1)
    new_li.pop()
    comb(new_li, idx + 1, cnt)


for i in range(1, T + 1):
    N, M = map(int, input().split())
    T = 2
    flag = [input() for _ in range(N)]
    copy = flag[:N - 1]
    new_li = []
    real_li = []
    comb(copy, 0, 0)
    INF = float('inf')
    min_cnt = INF
    for j in range(0, len(real_li), 2):
        w_len = real_li[j]
        b_len = real_li[j + 1]
        cnt = 0
        for w in range(w_len + 1):
            for k in range(M):
                if flag[w][k] != 'W':
                    cnt += 1

        for b in range(w_len + 1, b_len + 1):
            for k in range(M):
                if flag[b][k] != 'B':
                    cnt += 1

        for r in range(b_len + 1, N):
            for k in range(M):
                if flag[r][k] != 'R':
                    cnt += 1

        if cnt < min_cnt:
            min_cnt = cnt

    print(f'#{i} {min_cnt}')