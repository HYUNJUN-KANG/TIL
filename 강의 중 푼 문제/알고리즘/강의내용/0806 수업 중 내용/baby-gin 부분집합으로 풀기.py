# 원소수가 3개인 부분집합을 생성
# 1이 3개인 6자리 2진수 --> 0도 3개
# 자연스럽게 두 그룹으로 묶임

cards = [5, 4, 1, 2, 3, 6]
cards.sort()        # 정렬을 해놓으면 크기순으로 뽑히므로 비교하기 좋음

for subset in range(1 << 6):

    # 각 자리값을 확인
    A, B = [], []        # 1과 0에 해당하는 것들을 담기 위한 리스트
    for i in range(6):         # 2^0 ~ 2^5
        if subset & (1<<i):        # 1과 0인 경우 구분
            A.append(cards[i])
        else:
            B.append((cards[i]))

    if len(A) == len(B):
        print(A, B)