import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    t = int(input())
    li = [[0] * 10 for _ in range(10)]

    for i in range(t):
        li1 = list(map(int, input().split()))

        for r in range(li1[0], li1[2]+1):
            for c in range(li1[1], li1[3]+1):
                li[r][c] += li1[4]

    cnt = 0
    for r in range(10):
        for c in range(10):
           if li[r][c] == 3:
               cnt += 1

    print("#{} {}".format(tc, cnt))