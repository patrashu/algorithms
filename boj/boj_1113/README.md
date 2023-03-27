##  BOJ 1113 (G1)

### https://www.acmicpc.net/problem/1113
### Algorithm: DFS, BFS, Simulation


``` python
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def bfs(x, y, num):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    flag = True
    
    tmp = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = False
                continue
            
            if not visited[nx][ny] and a[nx][ny] <= num:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                tmp += 1
    if flag:
        cnt += tmp
    else:
        return
                    

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for num in range(1, 10):
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j] <= num and not visited[i][j]:
                    bfs(i, j, num)
                    
    print(cnt)
```

```python
import sys

sys.setrecursionlimit(10**5)

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y, tmp):
  global visited, flag, total_cnt

  if x == 0 and y == 0:
    flag = False

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and graph[nx][
        ny] <= tmp and not visited[nx][ny]:
      visited[nx][ny] = 1
      if flag:
        total_cnt += 1

      dfs(nx, ny, tmp)


def check(x):
  global flag, total_cnt
  for i in range(n + 2):
    for j in range(m + 2):
      if graph[i][j] <= x and not visited[i][j]:
        if i != 0 and j != 0:
          total_cnt += 1

        visited[i][j] = 1
        flag = True
        dfs(i, j, x)


if __name__ == '__main__':
  n, m = map(int, input().split())
  ## 입력
  a = [list(input().strip()) for _ in range(n)]
  graph = [[1] * (m + 2) for _ in range(n + 2)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      graph[i][j] = int(a[i - 1][j - 1])

  flag = True
  total_cnt = 0
  for i in range(1, 10):
    visited = [[0] * (m + 2) for _ in range(n + 2)]
    check(i)

  print(total_cnt)
```

- dfs 통과 못한 이유가 setrecursionlimit을 너무 크게 줘서 (앞으로 명심하길)

