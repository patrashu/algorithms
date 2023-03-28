##  BOJ 14502 (G4)

### https://www.acmicpc.net/problem/14502
### Algorithm: Implementation, BFS

```python
import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(new_field, birus):
  q = deque(birus)
  # searching
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < n and 0 <= ny < m and new_field[nx][ny] == 0:
        new_field[nx][ny] = 2
        q.append((nx, ny))

  # counting
  tmp = 0
  for i in range(n):
    tmp += new_field[i].count(0)

  return tmp
  

if __name__ == '__main__':
  n, m = map(int, input().split())
  field = []
  safe = []
  birus = []
  max_value = 0

  # define input
  for i in range(n):
    a = list(map(int, input().split()))    
    for j in range(m):
      if a[j] == 2:
        birus.append((i, j))
      elif a[j] == 0:
        safe.append((i, j))
    field.append(a)

  # search
  candits = list(combinations(safe, 3))
  for candit in candits:
    new_field = copy.deepcopy(field)
    for px, py in candit:
      new_field[px][py] = 1
      
    max_value = max(max_value, bfs(new_field, birus))

  print(max_value)
```