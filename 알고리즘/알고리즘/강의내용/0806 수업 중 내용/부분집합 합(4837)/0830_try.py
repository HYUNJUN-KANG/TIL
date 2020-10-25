# import sys
# sys.stdin = open('input.txt', 'r')
#
# N, K = map(int, input().split())

# N = 부분집합 원소 수
# K = 부분집합의 합
T = int(input())
A = [i for i in range(n)]

n = len(A)

for tc in range(1, T+1):

    for i in range(1<<n):

        b = []        # 부분집합을 담을 리스트

        for j in range(n):
            if i & (1<<j):
                b.append(A[j])
        if len(b) == N and sum(b) == K:
            c.append(b)

    print("#{} {}".format(tc, len(c))):