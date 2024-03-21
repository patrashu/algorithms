### 프로그래머스 '경주로 건설' (레벻 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/67259

### Algorithm: Simulation, BFS

```python
from collections import deque, defaultdict

def solution(board):
    answer = int(1e9)
    r, c = len(board), len(board[0])
    direc = { 0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1) }
    dq = deque([(0, 0, 1, 0), (0, 0, 2, 0)]) # x, y, dir, cost
    visited = defaultdict(int)
    visited[(0, 0, 1)] = 0
    visited[(0, 0, 2)] = 0
    
    while dq:
        cx, cy, cdir, cost = dq.popleft()
        if cost > visited[(cx, cy, cdir)]:
            continue
            
        if (cx, cy) == (r-1, c-1):
            answer = min(answer, cost)
            continue
        
        # 직진 회전
        for ndir, ncost in [(cdir, 100), ((cdir-1)%4, 600), ((cdir+1)%4, 600)]:
            dx, dy = direc[ndir]
            nx, ny = cx+dx, cy+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] == 1:
                continue
            if not visited[(nx, ny, ndir)] or visited[(nx, ny, ndir)] > cost+ncost:
                visited[(nx, ny, ndir)] = cost+ncost
                dq.append((nx, ny, ndir, cost+ncost))
    
    return answer
```
