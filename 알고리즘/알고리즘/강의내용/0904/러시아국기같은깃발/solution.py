#러시아 국기 같은 깃발
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    INF = float('inf') #많이 큰 수를 표현할 때 사용
    min_cnt = INF   #바뀌는 영역의 최소값을 저장하기 위한 변수
    #흰색 , 파란색, 빨간색 영역 구분하기
    #흰색, 파란색 영역이 끝나는 인덱스로 구분하자!
    # 흰색이 끝날 수 있는 인덱스 : 0~ N-2-1
    # 파란색이 끝날 수 있는 인덱스 : 흰색영역 +1 ~ N-1-1
    # 빨간색 영역 :파란색 영역 +1~ N-1
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            # 여기서 세개의 영역으로 구분할 수 있음
            # 0~i, i+1~j, j+1~끝
            cnt = 0
            # 흰색 영역 순회하면서 바꿔야할 개수 세기
            for w in range(0,i+1):  #i가 흰색영역의 끝이니 i를 포함해야함
                for k in range(M):
                    if flag[w][k] != 'W':
                        cnt += 1
            # 파란 영역 순회하면서 바꿔야할 개수 세기
            for b in range(i+1,j+1):
                for k in range(M):
                    if flag[b][k] != 'B':
                        cnt += 1
            # 빨간 영역 순회하면서 바꿔야할 개수 세기
            for r in range(j+1,N):
                for k in range(M):
                    if flag[r][k] != 'R':
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt
    print("#{} {}".format(tc,min_cnt))