# BOJ 2206 (G3)

## https://www.acmicpc.net/problem/2206

### Algorithm: BFS

``` python
import sys
from collections import deque
INF = 1e9

n, m = map(int, input().split())
graph = [[int(i) for i in list(map(str, input()))] for _ in range(n)]
ans = [[INF] * m for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque([(0, 0, False)])  # x, y, is_wall
visited[0][0] = [True, True]
ans[0][0] = 1

if [n, m] == [1, 1]:
  print(1)
  sys.exit(0)

# 탐색 진행
while queue:
  cx, cy, is_wall = queue.popleft()
  if [cx, cy] == [n - 1, m - 1]:
    break
  for i in range(4):
    nx, ny = cx + dx[i], cy + dy[i]
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][is_wall]:
      if graph[nx][ny] == 0:
        ans[nx][ny] = ans[cx][cy] + 1
        queue.append((nx, ny, is_wall))
        visited[nx][ny][is_wall] = True
      elif graph[nx][ny] == 1 and is_wall is False:
        ans[nx][ny] = ans[cx][cy] + 1
        queue.append((nx, ny, True))
        visited[nx][ny][is_wall] = True

print(-1 if ans[n - 1][m - 1] == INF else ans[n - 1][m - 1])
```
