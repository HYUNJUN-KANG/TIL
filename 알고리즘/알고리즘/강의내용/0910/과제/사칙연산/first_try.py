import sys
sys.stdin = open('input.txt', 'r')

def tree_order(v):
    if v:
        v1 = tree_order(tree[v][1])
        v2 = tree_order(tree[v][2])

        if v1 and v2:
            return cal[tree[v][0]](v1, v2)

        return tree[v][0]

T = 10

for tc in range(1, T+1):
    N = int(input())
    tmp = [input().split() for _ in range(N)]

    tree = [[0] * 4 for _ in range(N + 1)]

    cal = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    for i in range(N):
        node, value, *child = tmp[i]
        v = int(node)

        if value in cal:
            tree[v][0] = value

            lc, rc = int(child[0]), int(child[1])

            tree[v][1], tree[v][2] = lc, rc

            tree[lc][3] = tree[rc][3] = v

        else:
            tree[v][0] = int(value)


    result = int(tree_order(1))
    print("#{} {}".format(tc, result))