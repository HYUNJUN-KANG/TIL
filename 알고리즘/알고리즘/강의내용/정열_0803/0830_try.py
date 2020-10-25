def counting_sort(A, B, k):
    C = [0] * k
    # 카운팅
    for i in range(0, len(B)):
        C[A[i]] += 1

    # 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]

    # sort
    for i in range(len(B)-1, 0, -1):





    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, 0, -1):
        B[C[A[i]-1]] = A[i]
        C[A[i]] -= 1

