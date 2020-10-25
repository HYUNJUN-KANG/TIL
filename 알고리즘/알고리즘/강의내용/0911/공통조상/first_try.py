import sys
sys.stdin = open('input.txt', 'r')

def in_order(idx):
    global cnt
    if left[idx] != 0:
        cnt += 1
        in_order(left[idx])
    if right[idx] != 0:
        cnt += 1
        in_order(right[idx])


T = int(input())
for tc in range(1, T + 1):

    V, E, P, C = map(int, input().split())
    left = [0 for _ in range(V + 2)]
    right = [0 for _ in range(V + 2)]
    visited = [0] * (V + 2)

    node = list(map(int, input().split()))

    cnt = 1
    for i in range(0, E * 2, 2):
        parent = node[i]
        child = node[i + 1]
        visited[child] = parent

        if left[parent] != 0:
            right[parent] = child

        else:
            left[parent] = child

    li_1 = [visited[P]]

    for i in range(len(visited)):

        if visited[li_1[-1]] != 0:
            li_1.append(visited[li_1[-1]])

    li_2 = [visited[C]]

    for i in range(len(visited)):
        if visited[li_2[-1]] != 0:
            li_2.append(visited[li_2[-1]])

    s = 1

    for i in range(min(len(li_1), len(li_2))):
        if li_1[::-1][i] != li_2[::-1][i]:
            s = visited[li_1[::-1][i]]
            break

    in_order(s)

    print('#%d %d %d' % (tc, s, cnt))
