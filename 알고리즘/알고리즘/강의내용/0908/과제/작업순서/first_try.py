import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())

    li_sample = list(map(int, input().split()))

    li = [[] for _ in range(V+1)]

    visited = [True for _ in range(V+1)]

    for i in range(E):
        r = li_sample[2*i]
        c = li_sample[(2*i)+1]

        li[c].append(r)

    result = []

    while True:

        if len(result) == V:
            break

        for i in range(1, V+1):
            if visited[i]:
                for j in li[i]:
                    if visited[j]:
                        break
                else:
                    visited[i] = False
                    result.append(i)
    print("#{}".format(tc), end=' ')
    print(*result)