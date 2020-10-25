import sys
sys.stdin = open('input.txt', 'r')

def heappop(value):
    global heapcount
    result = heap[1]

    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= heapcount:
        if heap[child] > heap[child+1]:
            child = child + 1

    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:
            if heap[child] > heap[child+1]:
                child = child + 1

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tmp_li = list(map(int, input().split()))
    size = len(tmp_li)

    heap = [0] * 128
    heapcount = 0

    for i in tmp_li:
        heappop(i)


