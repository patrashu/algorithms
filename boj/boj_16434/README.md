## BOJ 16434 (G4)

### https://www.acmicpc.net/problem/16434

### Algorithm: Implementation

```python
import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
INF = 1e9
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

if __name__ == '__main__':
  ## 입력
  n, m = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(n)]

  ## 거리 초기화 및 큐 생성
  dist = [[INF] * m for _ in range(n)]
  queue = deque()

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        dist[i][j] = 0
        queue.append((i, j))

  ## bfs 탐색 진행
  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == INF:
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))

  max_num = 0
  for num in dist:
    max_num = max(max_num, max(num))

  print(max_num)

```
