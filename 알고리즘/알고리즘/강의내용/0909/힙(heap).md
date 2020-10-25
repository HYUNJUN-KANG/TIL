# 힙(heap)



## heappush

```python
tmp = [7, 2, 4, 3, 1, 2, 5]
size = len(tmp)
heap = [0] * 128
heapcount = 0   # 마지막 노드의 위치를 나타내는 인덱스
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    
    # 만약에 새롭게 정의된 자식이 부모노드보다 작으면,
    # 부모노드와 위치를 바꿔줘야 한다.
    
    cur = heapcount
    parent = cur // 2  #이진트리를 배열로 표현할 때 부모노드의 인덱스는 자식노드 인덱스// 2
    
    # 부모노드가 더 크거나, 부모노드가 root 일 때 까지 계속 반복
    # if heap[cur] < heap[parent]:
    #    heap[parent], heap[cur] = heap[cur], heap[parent]
    
    while parent > 0 and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2
        
for i in tmp:
    heappush(i)

print(heap)
```



## heappop (최소힙)

```python
tmp = [7,2,4,3,1,6,5]
size = len(tmp)
heap = [0] * 128
heapcount = 0 #현재 마지막 노드가 들어있는 인덱스

def heappop():
    global heapcount
	result = heap[1]   # root를 없애기 전에 저장 for 반환
    
    # heap의 마지막 인덱스에 있는 노드를 root로 바꿔줌
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1   # 마지막 노드는 없어짐
    
    # 자식들 중에서 작은 애가 부모가 되어야 함
    parent = 1
    child = parent * 2  # 부모와 위치를 바꿔줄 자식의 인덱스
    # 오른쪽 자식이 있으면, 오른쪽이 작은지 왼쪽이 작은지 비교
    if child + 1 <= heapcount:
        if heap[child] > heap[child+1]:
            child = child + 1
            
    # 만약에 자식과 부모노드를 비교해서 자식노드가 더 작으면 바꿔줌
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:
            if heap[child] > heap[child + 1]:
                child = child + 1
    
    return result

for i in range(len(tmp)):
    print(heappop())
	print(heap)		
```

