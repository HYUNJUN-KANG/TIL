T = int(input())

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize; p = hsize // 2

    while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p; p = c // 2


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    H = [0] * (N+1)
    hsize = 0