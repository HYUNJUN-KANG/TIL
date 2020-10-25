import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

arr = [i for i in range(1, 12+1)]
ans = 0

for bits in range(1, 1<<12):
    cnt = S = 0

    for i in range(12):
        if bit & (1<<i):
            cnt += 1
            S += arr[i]

        if cnt == N and S == K:
            ans += 1