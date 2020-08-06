T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input())               # 공백 없으면 split없이 list 가능.
    # [4, 9, 6, 7, 9]


    # 배열의 인덱스에 해당하는 카드가 몇장인지 저장하는 배열을 만든다. 각 카드가 몇장인지 표시할 수 있다.
    # 0~9의 숫자가 들어오므로,

    counts = [0] * 10           # [0, 0 , 0 ,00 ,0, 0, 0]
    for i in range(N):
        counts[cards[i]] += 1         # 카드의 값과 일치하는 counts 인덱스에 +1 을 해주면서 숫자를 세준다.

    max_v = counts[0]
    max_idx = 0

    for i in range(len(counts)):

        if max_v <= counts[i]:
            max_v = counts[i]
            max_idx = i

    print("#%d" % tc, max_idx, max_v)
