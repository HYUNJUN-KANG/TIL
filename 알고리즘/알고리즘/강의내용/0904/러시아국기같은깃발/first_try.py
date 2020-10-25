import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    li = [input() for _ in range(N)]
    INF = float('inf')
    min_cnt = INF

    for i in range(0,N-2):
        for j in range(i+1,N-1):

            cnt = 0

            for w in range(0,i+1):
                for k in range(M):
                    if li[w][k] != 'W':
                        cnt += 1

            for b in range(i+1,j+1):
                for k in range(M):
                    if li[b][k] != 'B':
                        cnt += 1

            for r in range(j+1,N):
                for k in range(M):
                    if li[r][k] != 'R':
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt
    print("#{} {}".format(tc,min_cnt))