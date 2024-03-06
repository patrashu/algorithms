### 프로그래머스  '무인도 여행' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/154540

### BFS


```python
from collections import deque

def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    visited = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if visited[i][j] or maps[i][j] == 'X':
                continue                
            visited[i][j] = True
            dq = deque([(i, j)])
            cur_sum = int(maps[i][j])
            while dq:
                cx, cy = dq.popleft()
                for k in range(4):
                    nx, ny = cx+dx[k], cy+dy[k]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if visited[nx][ny] or maps[nx][ny] == 'X':
                        continue
                        
                    visited[nx][ny] = True
                    cur_sum += int(maps[nx][ny])
                    dq.append((nx, ny))
            answer.append(cur_sum)
                        
    return sorted(answer) if answer else [-1]
```    