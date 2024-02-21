##  Leetcode week3-2

### https://leetcode.com/problems/01-matrix/description/
### Algorithm: DFS, Tree

```python
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        visited = [[False]*c for _ in range(r)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        dq = deque()

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    flag = False
                    for k in range(4):
                        nx, ny = i+dx[k], j+dy[k]
                        if nx < 0 or nx >= r or ny < 0 or ny >= c:
                            continue
                        if mat[nx][ny] == 0:
                            flag = True
                    if flag:
                        visited[i][j] = True
                        dq.append((i, j, 1))
        
        next_q = deque()
        while True:
            while dq:
                cx, cy, dist = dq.popleft()
                for i in range(4):
                    nx, ny = cx+dx[i], cy+dy[i]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or mat[nx][ny] == 0:
                        continue
                    
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        mat[nx][ny] = dist+1
                        next_q.append((nx, ny, dist+1))

            if not next_q:
                break
            
            dq = next_q
            next_q = deque()

        return mat
```
