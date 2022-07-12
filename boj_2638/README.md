##  BOJ 2638 (G3)

### https://www.acmicpc.net/problem/2638
### Algorithm: Resursion, DFS, Simulation
#### Trial: 2 (By Python Recursive Error)

### Code 1 (2312ms)
```python
import sys
# sys.stdin = open('input.txt', 'rt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    global wall  

    if a[x][y] == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and not visited[nx][ny]:
                    wall.append((nx, ny))
                    visited[nx][ny] = 1
                    dfs(nx, ny)

    else:
        check = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if a[nx][ny] == 0:
                check += 1
        
        if check >= 2:
            del_queue.append((x, y))


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny)



if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []

    cnt_cheeze = 0 
    for i in range(n):
        a.append(list(map(int, input().split())))
        cnt_cheeze += sum(a[i])

    zero_cnt = n*m - cnt_cheeze
    cnt = 0

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while cnt_cheeze != 0:
        visited = [[0]*m for _ in range(n)]
        del_queue = []
        wall = []
        

        for i in range(n):
            for j in range(m):
                flag = True

                if a[i][j] == 0 and not visited[i][j]:
                    if i == 0 or j == 0 or i == n or j == m:
                        flag = False
                        visited[i][j] = 1
                        dfs(i, j)
                    else:
                        wall.append((i, j))
                        visited[i][j] = 1
                        dfs(i, j)
                
                if not flag: 
                    wall = []

        for x, y in wall:
            a[x][y] = 1

        for i in range(n):
            for j in range(m):
                if a[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = 1
                    dfs(i, j)
        
        cnt_cheeze -= len(del_queue)

        for x, y in del_queue:
            a[x][y] = 0
        
        for x, y in wall:
            a[x][y] = 0

        cnt += 1

    print(cnt)

```

### Code 2 (992ms)
```python
import sys
# sys.stdin = open('input.txt', 'rt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if a[nx][ny] != 0:
                a[nx][ny] += 1
            else:
                visited[nx][ny] = 1
                dfs(nx, ny)



if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []

    cnt_cheeze = 0 
    for i in range(n):
        a.append(list(map(int, input().split())))
        cnt_cheeze += sum(a[i])

    cnt = 0

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while cnt_cheeze != 0:
        visited = [[0]*m for _ in range(n)]
        dfs(0, 0)

        for i in range(n):
            for j in range(m):
                if a[i][j] >= 3:
                    a[i][j] = 0
                    cnt_cheeze -= 1
                elif a[i][j] > 0:
                    a[i][j] = 1

        cnt += 1

    print(cnt)


```
