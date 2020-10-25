import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

for i in range(num):
    a, b = map(int, input().split())

    for r in range(a, a+10):
        for c in range(b, b+10):
            li[r][c] = 1

area = 0
