##  BOJ 2638 (G3)

### https://www.acmicpc.net/problem/2638
### Algorithm: Resursion, DFS, Simulation
#### Trial: 2 (By Python Recursive Error)

### Code 1 (2312ms) (DFS)
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

### Code 2 (812ms) (DFS)
```python
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
      if graph[nx][ny] >= 1:
        graph[nx][ny] += 1
      else:
        visited[nx][ny] = 1
        dfs(nx, ny)


if __name__ == '__main__':
  ## 입력
  n, m = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]
  time = 0

  ## 탐색 시작
  while True:
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    dfs(0, 0)
    flag = 0

    ## 두 면 이상 접해있는 경우
    for i in range(n):
      for j in range(m):
        if graph[i][j] >= 3:
          graph[i][j] = 0
          flag = 1
        elif graph[i][j] == 2:
          graph[i][j] = 1
    
    ## 두 면 이상 접한 치즈가 1개 이상인 경우 
    if flag:
      time += 1
    else:
      break

  print(time)

```

### Code 3(BFS)(236ms)

```python
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs():
  q = deque()
  q.append((0, 0))
  visited[0][0] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
        if graph[nx][ny] >= 1:
          graph[nx][ny] += 1
        else:
          visited[nx][ny] = 1
          q.append((nx, ny))


if __name__ == '__main__':
  n, m = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]

  time = 0
  while True:
    visited = [[0] * m for _ in range(n)]
    bfs()
    flag = 0

    for i in range(n):
      for j in range(m):
        if graph[i][j] >= 3:
          graph[i][j] = 0
          flag = 1
        elif graph[i][j] == 2:
          graph[i][j] = 1
          
    if flag == 1:
      time += 1
    else:
      break

  print(time)


```