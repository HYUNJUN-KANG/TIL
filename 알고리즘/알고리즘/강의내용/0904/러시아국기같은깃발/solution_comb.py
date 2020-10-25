# 2개의 변수를 결정
# 결정된 변수 2개를 이용해서 3개의 영역을 순회
# 조합구하기:
# selected : 요소선택표시
# idx : 요소를 가리키기 위한 인덱스
# cnt : 선택된 요소의 개수를 세기위한 변수

def comb(selected,idx,cnt):
    global min_cnt
    if cnt == 2: # 2개의 행을 모두 골랐으면, 재귀 종료
        #세개의 영역을 구분해서, 색깔을 바꿔야할 칸수 세기
        i, j = -1, -1
        for k in range(N):
            if selected[k] == 1:
                # i에 값이 할당되지 않았으면, i에 k를 할당, i에 값이 할당되었으면 j에 k를 할당
                if i == -1:
                    i = k
                else:
                    j = k

        # i와 j가 결정되어 있음.

        cnt = 0
        # 흰색 영역 순회하면서 바꿔야할 개수 세기
        for w in range(0, i + 1):  # i가 흰색영역의 끝이니 i를 포함해야함
            for k in range(M):
                if flag[w][k] != 'W':
                    cnt += 1
        # 파란 영역 순회하면서 바꿔야할 개수 세기
        for b in range(i + 1, j + 1):
            for k in range(M):
                if flag[b][k] != 'B':
                    cnt += 1
        # 빨간 영역 순회하면서 바꿔야할 개수 세기
        for r in range(j + 1, N):
            for k in range(M):
                if flag[r][k] != 'R':
                    cnt += 1

        # cnt가 여태까지 계산했던 cnt 중에서 가장 작으면 정답으로 저장
        if min_cnt > cnt:
            min_cnt = cnt

        return

    #마지막행을 제외한 모든행을 선택하면, 재귀 종료
    if idx == N-1:
        return

    selected[idx] = 1
    comb(selected,idx+1,cnt+1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    selected = [0] * N
    min_cnt = 2500
    comb(selected, 0, 0)
    print("#{} {}".format(tc, min_cnt))