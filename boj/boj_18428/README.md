## BOJ 18428 (G5)

### https://www.acmicpc.net/problem/18428

### Algorithm: Bruteforce, Backtracking

```python
import sys
import copy
from itertools import combinations
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def check(new_f, st):
  flag = False
  ## 학생 위치 정보 확인
  for pos_x, pos_y in st:
    for i in range(4):
      x, y = dx[i], dy[i]
      nx, ny = pos_x, pos_y

      while True:
        nx, ny = nx + x, ny + y
        if 0 <= nx < n and 0 <= ny < n:
          if new_f[nx][ny] == 'X':
            continue
          elif new_f[nx][ny] == 'O':
            break
          elif new_f[nx][ny] == 'T':
            flag = True
            break
        else:
          break

      if flag:
        return

  if not flag:
    print("YES")
    sys.exit(0)


if __name__ == '__main__':
  n = int(input())
  fields = [list(input().strip().split()) for _ in range(n)]

  st = []
  x = []

  for i in range(n):
    for j in range(n):
      if fields[i][j] == 'S':
        st.append((i, j))
      elif fields[i][j] == "T":
        pass
      else:
        x.append((i, j))

  new_f = copy.deepcopy(fields)
  candidates = combinations(x, 3)
  for candi in candidates:
    for i, j in candi:
      new_f[i][j] = 'O'

    check(new_f, st)

    for i, j in candi:
      new_f[i][j] = 'X'

  print('NO')
```
