## BOJ 1261 (G4)

### https://www.acmicpc.net/problem/1261

### Algorithm: BFS

```python
import sys
from collections import deque


def main(field: list[int]):
  dq = deque([(0, 0, 0)])
  dp = [[sys.maxsize] * n for _ in range(m)]
  dp[0][0] = 0

  while dq:
    x, y, dist = dq.popleft()
    if dp[x][y] < dist:
      continue

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and dp[nx][ny] > dist + field[nx][ny]:
        dp[nx][ny] = dist + field[nx][ny]
        dq.append([nx, ny, dist+field[nx][ny]])

  return dp[-1][-1]


if __name__ == '__main__':
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  n, m = map(int, input().split())
  field = [list(map(int, input().strip())) for _ in range(m)]
  print(main(field))
```
