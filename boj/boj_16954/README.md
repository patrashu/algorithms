## BOJ 16954 (G3)

### https://www.acmicpc.net/problem/16954

### Algorithm: BFS

```python
import sys
from collections import deque

arr = [['*']*8 for _ in range(8)] + [list(map(str, input().strip())) for _ in range(8)]
queue = deque([(15, 0)])
time = 0
direc = [(-1, 0), (-1, 1), (0, 1), (0, -1), (-1, -1), (0, 0), (1, -1), (1, 0), (1, 1)]
visit = set()
visit.add((15, 0))

while time < 15:
  nq = deque()
  while queue:
    cx, cy = queue.popleft()
    if cx < 8 and cy == 7:
      print(1)
      sys.exit(0)
      
    for dx, dy in direc:
      nx, ny = cx+dx, cy+dy
      if 0 <= nx < 16 and 0 <= ny < 8:
        # 이동 못할 때
        if arr[nx][ny] == '#':
          continue
        # 이동할 수 있는데 한 칸 내려올 때 죽는 경우
        if arr[nx-1][ny] == '#':
          continue
        # 이동 가능 + 중력에도 죽지 않는 경우:
        if (nx-1, ny) not in visit:
          visit.add((nx-1, ny))
          nq.append((nx-1, ny))

  queue = nq
  time += 1
  
print(0)
```
