import sys
sys.stdin = open('input.txt', 'r')

def num(n):
    if n == 1:
        return 1

    elif n == 2:
        return 3
    return num(n-1) + num(n-2)*2

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cnt = num(N//10)

    print("#{} {}".format(tc, cnt))