

def perm(k, cur_sum):   # cur_sum: 0 ~ k-1
    global ans;
    if k == N:
         ans = min(ans, cur_sum)
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

for tc in range(1, int(input()) + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cols = [i for i in range(N)]

perm(0)