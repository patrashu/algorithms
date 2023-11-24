### 프로그래머스 'PCCP 기출문제' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/250136

### 세트, BFS


```python
from collections import deque, defaultdict

def solution(land):
    cnts = defaultdict(int)
    r, c = len(land), len(land[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    visited = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j], cnt = True, 1
                cols = set()
                cols.add(j)
                q = deque([(i, j)])
                
                while q:
                    cx, cy = q.popleft()
                    for k in range(4):
                        nx, ny = cx+dx[k], cy+dy[k]
                        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            cnt += 1
                            cols.add(ny)
                            q.append((nx, ny))
                
                for col in cols:
                    cnts[col] += cnt
    
    return sorted(cnts.items(), key=lambda x: -x[1])[0][1]
```    