# enumerate(a) : idx와 a값 둘다 출력 가능.



```python
def lonely(numbers):
    result = []
    
    for idx, num in enumerate(numbers):    # enumerate를 사용하여 index와 같이 표시.
        if idx == 0:
            result.append(num)
            
        if result[-1] != num:
            result.append(num)
        
    return result

lonely([1, 1, 3, 3, 0])
```

