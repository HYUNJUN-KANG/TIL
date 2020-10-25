import sys
sys.stdin = open('input.txt', 'r')

def tree(n):
    global cnt
    while n <= N:
        tree(n*2)
        li[n] = cnt

        cnt += 1
        tree(n*2 + 1)
        break
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [0 for _ in range(N+1)]
    cnt = 1
    tree(1)
    print("#{} {} {}".format(tc, li[1], li[N//2]))