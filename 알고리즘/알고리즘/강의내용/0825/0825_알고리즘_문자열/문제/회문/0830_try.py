import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = []
    result = []
    for i in range(n):
        li.append(input())

    for i in range(n):
        for j in range(n-m+1):
            if li[i][j:j+m] == li[i][j:j+m][::-1]:
                result.append(li[i][j:j+m])

    for i in range(n-m+1):
        for j in range(n):
            new_li = []
            for k in range(m):
                new_li.append(li[i+k][j])
            if new_li == new_li[::-1]:
                result.append(''.join(new_li))

    print(*result)


