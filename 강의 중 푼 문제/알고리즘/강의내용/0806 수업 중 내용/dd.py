arr = [3, 6, 7]

n = len(arr)      # 3

for i in range(1<<n):          # 1<<n = 2^3
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = ",")
    print()
print()