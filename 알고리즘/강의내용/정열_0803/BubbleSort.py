def BubbleSort(a):
    for i in range(len(a)-1, 0, -1)          # 4 3 2 1순으로 돎
        for i in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]   #Swap


data = [55, 7, 78, 12, 42]

BubbleSort(data)
print(data)



