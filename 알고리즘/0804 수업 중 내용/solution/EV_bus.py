T = int(input())

for tc in range(1, T+1):

    # K: 최대 이동가능 거리
    # N: 정류장 총 거리
    # M: 충전기 정류장 개수

    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))        # 정류장 시작과 끝이 포함되지 않은 충전기 목록
    stations.insert(0,0)         # 시작 정류장 추가
    stations.append(N)          # 마지막 정류장 추가

    # 충전기 목록 확인하면서, 충전 횟수 카운팅하기

    pos = 0      # 현재 위치
    for i in range(M+2):         # B/C 처음과 끝 두개의 정류장이 추가 됐으므로 +2.

        # 현재 정류장의 위치와 이전 정류장의 위치의 차이가 K보다 크다면 충전 불가능.
        if (stations[i] - stations[i-1]) > K:              # 이동 불가능
            cnt = 0
            break

        # 충전하려고 하는 정류장의 위치가 pos + K 보다 크다면, 이전 정류장에서 충전을 해야한다.
        if stations[i] > pos + K:
            pos = stations[i-1]         # 이전 정류장에서 충전을 하겠다.  -> pos의 위치가 이전 충전소 정류장의 위치가됨.
            cnt += 1

    print("#%d" % tc, cnt)
