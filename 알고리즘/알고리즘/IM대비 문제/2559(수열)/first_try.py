import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

li = list(map(int, input().split()))

sum_li = []
for i in range(0, len(li)-K+1):

    a = 0
    for j in range(i, K+i):
        a += li[j]

    sum_li.append(a)


print(max(sum_li))