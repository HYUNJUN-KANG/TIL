import sys

sys.stdin = open("input.txt", 'r')



T = 10

for tc in range(1, T+1):


    N = int(input())         # 테스트 케이스 길이

    buildings = list(map(int, input().split()))



# 각 건물의 왼쪽, 오른쪽 조망권을 구하고
# 옆, 옆옆 건물의 높이 중 더 높은 건물의 높이를
# 현재 건물의 높이에서 빼면, 각 방향의 조망권이 계산할 수 있다.
# 왼쪽, 오른쪽 조망권 중 더 작은 값이 건물의 조망권이 확보된 세대의 수이다.
# 단, 조망권의 크기는 1이상일 경우에만 생각한다.
    total = 0  # 전체 조망권

    for i in range(2, N-2):
        # 왼쪽 조망권
        left = 0
        left_view = 0
        if buildings[i-1] > buildings[i-2]:
            left = buildings[i-1]
        else:
            left = buildings[i-2]
        left_view = buildings[i] - left

        # 오른쪽 조망권
        right = 0
        right_view = 0
        if buildings[i + 1] > buildings[i + 2]:
            right = buildings[i + 1]
        else:
            right = buildings[i + 2]
        right_view = buildings[i] - right

        # 왼쪽과 오른쪽 조망권 중에 조망권이 없는 경우는 선택 X
        if left_view <= 0 or right_view <= 0:
            continue

        #  왼쪽, 오른쪽 중 작은값 선택하여 전체 조망권에 더한다.
        if left_view > right_view:
            total += right_view
        else:
            total += left_view

    print("#%d" %tc, total)
    print(f'#{tc} {total}')
