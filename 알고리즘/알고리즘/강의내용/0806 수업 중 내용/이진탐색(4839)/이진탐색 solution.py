def binarySearch(s, e, key):
    l, r = s, e
    cnt = 0
    while l <= r:
        mid = int((l + r) / 2)
        cnt += 1
        if key == mid:
            break

        elif key < mid:
            r = mid         # 원래는 +1 해줘야하지만 문제에서 주어진 조건에 따름

        else:
            l = mid         # 원래는 +1 해줘야하지만 문제에서 주어진 조건에 따름

    return cnt