```python
for tc in range(1, T+1):
    arr = input()
    S = []
    
    for ch in arr:
       	if not S or ch != S[-1]:  	# 빈 스택이 아닌 경우
            S.append(ch) 	# ch와 S[-1] 비교해서 다르면 S에 PUSH
        else:
            S.pop() 	# ch와 S[-1] 비교해서 같으면 ch와 S[-1] 버린다.
    
    print(len(S))
```

