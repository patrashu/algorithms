### 프로그래머스 '블록 이동하기' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/60063

### Algorithm: Implementation, BFS

```python
"""
4방향 이동 + 4방향 회전 고려
"""
from collections import deque, defaultdict

def solution(board):
    answer = 0
    r, c = len(board), len(board[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    visited = defaultdict(int)
    q = deque([(0, 0, 0, 1, 0, 0)]) # x1,y1,x2,y2,shape,depth
    visited[(0,0,0,1)] = 0
    while q:
        x1, y1, x2, y2, shape, cost = q.popleft()
        if (x2, y2) == (r-1, c-1):
            answer = cost
            break
        # move
        for i in range(4):
            nx1, ny1, nx2, ny2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
            # out of boundary
            if not (0 <= nx1 < r and 0 <= ny1 < c) or not (0 <= nx2 < r and 0 <= ny2 < c):
                continue
                
            # check wall
            if board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
                continue
                
            # check visited
            if (nx1, ny1, nx2, ny2) not in visited or visited[(nx1, ny1, nx2, ny2)] > cost+1:
                visited[(nx1, ny1, nx2, ny2)] = cost+1
                q.append((nx1, ny1, nx2, ny2, shape, cost+1))
                
        # rotate 'ㅡ' shape
        npts = None
        if shape == 0:
            npts = [
                [x1-1, y1, x1, y1, x2-1, y2], 
                [x1, y1, x1+1, y1, x2+1, y2],
                [x2-1, y2, x2, y2, x1-1, y1],
                [x2, y2, x2+1, y2, x1+1, y1]                
            ]
        # rotate 'ㅣ' shape
        else:
            npts = [
                [x1, y1-1, x1, y1, x2, y2-1],
                [x1, y1, x1, y1+1, x2, y2+1],
                [x2, y2-1, x2, y2, x1, y1-1],
                [x2, y2, x2, y2+1, x1, y1+1]
            ]
            
        for nx1, ny1, nx2, ny2, chx, chy in npts:
            if not (0 <= nx1 < r and 0 <= ny1 < c) or not (0 <= nx2 < r and 0 <= ny2 < c):
                continue
            if board[nx1][ny1] == 1 or board[nx2][ny2] == 1 or board[chx][chy] == 1:
                continue
            if (nx1, ny1, nx2, ny2) not in visited or visited[(nx1, ny1, nx2, ny2)] > cost+1:
                visited[(nx1, ny1, nx2, ny2)] = cost+1
                # shape change
                if shape == 0:
                    q.append((nx1, ny1, nx2, ny2, 1, cost+1))
                else:
                    q.append((nx1, ny1, nx2, ny2, 0, cost+1))

    return answer
```
