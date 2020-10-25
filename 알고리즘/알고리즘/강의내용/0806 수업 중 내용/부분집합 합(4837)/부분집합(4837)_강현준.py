import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
A = []
for i in range(1, 13):
    A.append(i)



n = len(A)


for tc in range(1, T+1):
    N = list(map(int, input().split()))
    c = []
    num_1 = N[0]
    sum_1 = N[1]
    for i in range(1<<n):

        # 부분집합 담을 리스트를 생성 b = []
        b = []

        for j in range(n):
            if i & (1<<j):
                b.append(A[j])          #for 탈출 -> b 완벽한 부분집합
        if len(b) == num_1 and sum(b) == sum_1:
            c.append(b)

    print("#%d" % tc, len(c))



