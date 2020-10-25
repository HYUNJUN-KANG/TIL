T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())   # E 간선수, 노드수 = E+1
    # 노드 번호 1 ~ (E + 1)

    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2):    # arr[i] -----> arr[i+1]
        p, c = arr[i], arr[i+1]

        if L[p]: R[p] = c     # p의 왼쪽 자식이 차 있으면 오른쪽에다가 채우고
        else: L[p] = c         # 왼쪽이 비어있으면 왼쪽에다가 채우자
        P[c] = p            # c의 부모정보를 p로 설정하자

    def traverse(v):
        if v == 0: return 0
        l = traverse(L[v])
        r = traverse(R[v])

        return l + r + 1

    traverse(N)
    print(ans)
