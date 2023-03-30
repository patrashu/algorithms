##  BOJ 16234 (G5)

### https://www.acmicpc.net/problem/16234
### Algorithm: Implementation, BFS

```python
import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited, cnt, pt):
  q = deque([(x, y)])
  pt.append((x, y))

  while q:
    cx, cy = q.popleft()
    visited[cx][cy] = cnt

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if l <= abs(field[nx][ny] - field[cx][cy]) <= r:
          visited[nx][ny] = cnt
          q.append((nx, ny))
          pt.append((nx, ny))

  if len(pt) == 1:
    visited[x][y] = 0

  return visited, pt

  
def fill_value(field, pts):
  for pt in pts:
    tmp = 0
    for x, y in pt:
      tmp += field[x][y]

    tmp //= len(pt)
    for x, y in pt:
      field[x][y] = tmp

  return field


if __name__ == '__main__':
  n, l, r = map(int, input().split())
  field = [list(map(int, input().split())) for _ in range(n)]
  ans = 0
  cnt = 1

  while True:
    visited = [[0] * n for _ in range(n)]
    pts = []

    for i in range(n):
      for j in range(n):
        # 방문 안했다면
        if not visited[i][j]:
          pt = []
          # 탐색 후 결과가 동일하다면
          visited, pt = bfs(i, j, visited, cnt, pt)
          if visited[i][j] != 0:
            pts.append(pt)
            cnt += 1
            
    exit_value = 0
    for k in range(n):
      exit_value += visited[k].count(0)

    if exit_value == n*n:
      break

    field = fill_value(field, pts)
    ans += 1

  print(ans)
```