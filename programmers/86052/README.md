### 프로그래머스 '빛의 경로 사이클' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/86052

### Algorithm: BFS


```python
""" 시뮬레이션
S => 직진, L => 좌회전, R => 우회전
Cycle을 찾아라

각 pos마다 4방향 visited flag 필요
500*500*4 -> 100만 => O(n)
"""
from collections import deque

def solution(grid):
    answer = []
    r, c= len(grid), len(grid[0])
    direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[[False]*4 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                dq = deque([(i, j, k, 0)]) # x, y, direction, cost
                visited[i][j][k] = True
                while dq:
                    cx, cy, k, cost = dq.popleft()
                    dx, dy = direc[k]
                    nx, ny = (cx+dx)%r, (cy+dy)%c
                    nd = k
                    if grid[nx][ny] == 'L':
                        nd = (k-1)%4
                    elif grid[nx][ny] == 'R':
                        nd = (k+1)%4
                    
                    if visited[nx][ny][nd]:
                        answer.append(cost+1)
                        break
                    visited[nx][ny][nd] = True
                    dq.append((nx, ny, nd, cost+1))

    return sorted(answer)
```