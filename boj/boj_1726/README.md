##  BOJ 1726 (G3)

### https://www.acmicpc.net/problem/1726
### Algorithm: BFS


``` python
#import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
change = [(2, 3), (2, 3), (0, 1), (0, 1)]

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
sr, sc, sd = list(map(int, input().split()))
er, ec, ed = list(map(int, input().split()))

## BFS
q = deque()
q.append([sr-1, sc-1, sd-1, 0])
visited[sr-1][sc-1][sd-1] = 1

while q:
  cx, cy, cd, cost = q.popleft()
  if [cx, cy, cd] == [er-1, ec-1, ed-1]:
    print(cost)
    break

  ## straight
  for move in range(1, 4):
    nx, ny, nd = cx + dx[cd]*move, cy + dy[cd]*move, cd
    ## out of range or wall
    if nx < 0 or nx >= n or ny < 0 or ny >= m or field[nx][ny] == 1:
      break
    ## visited
    if visited[nx][ny][nd]:
      continue
    ## not visited
    visited[nx][ny][nd] = 1
    q.append((nx, ny, nd, cost+1))

  ## turn left/right
  for move in change[cd]:
    if visited[cx][cy][move]:
      continue
    visited[cx][cy][move] = 1
    q.append((cx, cy, move, cost+1))   
```


