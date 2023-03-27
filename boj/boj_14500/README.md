##  BOJ 16236 (G4)

### https://www.acmicpc.net/problem/14500
### Algorithm: Simulation, BruteForce, DFS


### 통과한 code (BruteForce)
```python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n,m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
tets = [
  [(0,0), (0,1), (1,0), (1,1)],
  [(0,0), (0,1), (0,2), (0,3)],
  [(0,0), (1,0), (2,0), (3,0)],
  [(0,0), (0,1), (0,2), (1,0)], 
  [(1,0), (1,1), (1,2), (0,2)],
  [(0,0), (1,0), (1,1), (1,2)],
  [(0,0), (0,1), (0,2), (1,2)],
  [(0,0), (1,0), (2,0), (2,1)],
  [(2,0), (2,1), (1,1), (0,1)],
  [(0,0), (0,1), (1,0), (2,0)], 
  [(0,0), (0,1), (1,1), (2,1)],
  [(0,0), (0,1), (0,2), (1,1)],
  [(1,0), (1,1), (1,2), (0,1)],
  [(0,0), (1,0), (2,0), (1,1)],
  [(1,0), (0,1), (1,1), (2,1)],
  [(1,0), (2,0), (0,1), (1,1)],
  [(0,0), (1,0), (1,1), (2,1)],
  [(1,0), (0,1), (1,1), (0,2)],
  [(0,0), (0,1), (1,1), (1,2)]
]
ans = 0

def find_max(x, y, tets):
  global ans
  for i in range(19):
    res = 0
    for j in range(4):
      nx = x + tets[i][j][0]
      ny = y + tets[i][j][1]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        break
      res += field[nx][ny]

    ans = max(ans, res)

for i in range(n):
  for j in range(m):
    find_max(i, j, tets)

print(ans)
```

### 통과한 case (DFS)
```python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# ㅗ 제외
def dfs(i, j, dsum, cnt):
  global max_value
  if cnt == 4:
    max_value = max(max_value, dsum)
    return

  for p in range(4):
    nx = i + move[p][0]
    ny = j + move[p][1]

    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx, ny, dsum+field[nx][ny], cnt+1)
      visited[nx][ny] = False

# ㅗ 
def exce(i, j):
  global max_value
  for p in range(4):
    tmp = field[i][j]
    for k in range(3):
      t = (p+k) % 4
      nx = i + move[t][0]
      ny = j + move[t][1]

      if not (0 <= nx < n and 0 <= ny < m):
        tmp = 0
        break
      tmp += field[nx][ny]
    max_value = max(max_value, tmp)
  

if __name__ == '__main__':
  n,m = map(int, input().split())
  field = [list(map(int, input().split())) for _ in range(n)]
  visited = [[0]*m for _ in range(n)]
  max_value = 0

  for i in range(n):
    for j in range(m):
      visited[i][j] = True
      dfs(i, j, field[i][j], 1)
      visited[i][j] = False
      
      exce(i, j)

  print(max_value)
```

### 통과 못한 code
``` python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def rotate_map(n, m, field):
  new_field = [[0]*n for _ in range(m)]
  
  for i in range(n):
    for j in range(m):
      new_field[m-j-1][i] = field[i][j]

  return new_field

def cal_max(n, m, field, tets):
  max_value = 0
  for poly in tets:
    xm, ym = poly[4]
    for i in range(0, n-xm):
      for j in range(0, m-ym):
        tmp = 0
        for k in range(4):
          tmp += field[poly[k][0]+i][poly[k][1]+j]
        max_value = max(max_value, tmp)
    
  return max_value      


if __name__ == '__main__':
  n,m = map(int, input().split())
  field = [list(map(int, input().split())) for _ in range(n)]

  # points + xmax + ymax
  tets = [
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]
  ]
  ans = 0
  
  for i in range(4):
    tmp_r, tmp_c = len(field), len(field[0])
    ans = max(ans, cal_max(tmp_r, tmp_c, field, tets))
    field = rotate_map(tmp_r, tmp_c, field)

  print(ans)
```