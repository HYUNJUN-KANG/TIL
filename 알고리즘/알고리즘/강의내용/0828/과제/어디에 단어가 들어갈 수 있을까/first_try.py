import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_cnt= [0]*(N+1)
    for i in range(N):
        cnt = 0
        bf = 0
        for j in range(N):
            if bf == 0 and li[i][j] == 1:
                if cnt:
                    li_cnt[cnt] += 1
                cnt = 1
            elif bf == 1 and li[i][j] == 1:
                cnt += 1
            bf = li[i][j]

        if cnt:
            li_cnt[cnt] += 1

    for j in range(N):
        cnt = 0
        bf = 0
        for i in range(N):
            if bf == 0 and li[i][j] == 1:
                if cnt:
                    li_cnt[cnt] += 1
                cnt = 1
            elif bf == 1 and li[i][j] == 1:
                cnt += 1
            bf = li[i][j]

        if cnt:
            li_cnt[cnt] += 1

    print("#{} {}".format(tc, li_cnt[M]))



