import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    queue = []
    queue.append(li[0])

    for i in range(1, M+1):
        j = i % N
        queue.pop(0)
        queue.append(li[j])

    print("#{} {}".format(tc, queue[0]))
