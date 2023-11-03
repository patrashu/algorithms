## BOJ 2599 (G5)

### https://www.acmicpc.net/problem/2589

### Algorithm: Brute Force / BFS

```python
"""
N*M Matrix , L(Land) / W(Ocean)
Can move four directions (up, down, left, right)
Each move takes one hour.
"""
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def bfs(i: int, j: int) -> int:
    q = deque()
    q.append((i, j))
    cnt = 0
    visited[i][j] = 1
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or field[nx][ny]=='W':
                continue
            
            if not visited[nx][ny]:
                visited[nx][ny] = visited[cx][cy]+1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))
    return cnt-1


n, m = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

for i in range(n):
    for j in range(m):
        if field[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            ans = max(ans, bfs(i, j))

print(ans)
```
