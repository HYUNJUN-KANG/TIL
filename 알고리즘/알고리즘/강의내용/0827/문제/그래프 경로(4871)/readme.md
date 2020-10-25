```python
import sys
sys.stdin = open('input.txt', 'r')


def dfs(v):
    global final
    if visited[v] == 1:
        return
    visited[v] = 1

    for i in range(1, V+1):

        if adj[v][i] == 1:
            if i == e:
                final = 1
                return
            else:
                dfs(i)


T = int(input())



for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        x, y = map(int, input().split())
        adj[x][y] = 1


    visited = [0]*(V+1)

    s, e = map(int, input().split())

    final = 0

    dfs(s)



    print("#{} {}".format(tc, final))
```





```python
for i in range(E):
        x, y = map(int, input().split())
        adj[x][y] = 1
```

`adj[x][y] = 1`만 해주어야 한다.

### `adj[y][x]=1`까지 한다면은 되돌아가면서 모든 경로가 이어지게 된다!!!!!!!!!!!!