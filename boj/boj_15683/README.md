##  BOJ 15683 (G4)

### https://www.acmicpc.net/problem/15683
### Algorithm: Simulation, Implement, DFS

```python
import sys
import copy
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


min_value = 1e9
n, m = map(int, input().split())
cctv = []
field = []
mode = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [0, 3]],
  [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

for i in range(n):
  tmp = list(map(int, input().split()))
  field.append(tmp)
  for j in range(m):
    if tmp[j] in [1, 2, 3, 4, 5]:
      cctv.append([tmp[j], i, j])

def fill(field, mm, x, y):
  for i in mm:
    nx, ny = x, y
    while True:
      nx += dx[i]
      ny += dy[i]
      if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != 6:
        if field[nx][ny] == 0:
          field[nx][ny] = 7
      else:
        break
          

def dfs(depth, field):
  global min_value

  if depth == len(cctv):
    count = 0
    for i in range(n):
      count += field[i].count(0)

    min_value = min(min_value, count)
    return

  c_field = copy.deepcopy(field)
  cctv_num, x, y = cctv[depth]
  for i in mode[cctv_num]:
    fill(c_field, i, x, y)
    dfs(depth+1, c_field)
    c_field = copy.deepcopy(field)


dfs(0, field)
print(min_value)
```