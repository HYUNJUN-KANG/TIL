import sys
sys.stdin = open('input.txt', 'r')

def tree_li(i):
    if i > N:
        return

    tree_li(2 * i)
    result.append(tree[i])
    tree_li(2 * i + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    li = [input().split() for _ in range(N)]

    # print(li)

    tree = [0] * (N + 1)
    for i in range(N):
        node, text, *child = li[i]
        tree[int(node)] = text

    result = []
    tree_li(1)    # node가 1부터 시작

    final_result = "".join(result)

    print("#{} {}".format(tc, final_result))
