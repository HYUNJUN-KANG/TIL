```python
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

B = input()
C = []
for i in range(len(B)):
    
    C.append(B[i])
    
    F = list(map(int, C))
    
	D = {}
for j in F:
    
    if j in D.keys():
        D[j] = 1
    elif j in D.keys():
        D[j] += 1
        
max_key = 0
max_val = 0

for key, val in D.items():
    
    if val > max_val:
        max_val = val
        max_key = int(key)
        
    elif val == max_val:
        if val > max_val:
            max_key = int(key)
        
```

