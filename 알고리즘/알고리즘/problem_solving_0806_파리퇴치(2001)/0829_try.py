import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(N)]


    li_value = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            value = 0
            for j in range(M):
                for k in range(M):
                    value += li[r+j][c+k]
            li_value.append(value)
    result = max(li_value)
    print("#{} {}".format(tc, result))