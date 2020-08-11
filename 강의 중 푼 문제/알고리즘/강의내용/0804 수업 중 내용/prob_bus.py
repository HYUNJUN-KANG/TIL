import sys
sys.stdin = open('input.txt', 'r')


T = int(input())



for tc in range(1, T+1):

    K, N ,M = map(int, input().split())

    B = list(map(int, input().split()))

    fuel = K
    now_pos = 0
    es_cnt = 0
    cnt = 0

    while now_pos < N:
        for s in B:
            dist = s - now_pos
            if fuel >= dist:
                now_pos += dist
                fuel -= dist
                if now_pos >= N:
                    break
                if B[es_cnt + 1] - B[es_cnt] > fuel:
                    fuel = K
                    cnt += 1
                es_cnt += 1
            else:
                cnt = 0
                break
        if cnt == 0:
            break

    print(f'#{tc}, {cnt}')
