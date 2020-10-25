import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    li = list(map(int, input().split()))

    for i in range(M):
        a = li.pop(0)
        li.append(a)


    print(li[0])