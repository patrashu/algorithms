### 프로그래머스  '미로탈출 명령어' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/150365

### 구현, 탐색


```python
from collections import deque

def solution(n, m, x, y, r, c, k):
    queue = deque()
    queue.append([x, y, 0, ''])
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direc_dict = {0:"d", 1:"l", 2:"r", 3:"u"}
    
    while queue:
        cx, cy, c_cost, direc = queue.popleft()
        if (cx, cy) == (r, c) and (k-c_cost)%2 == 1:
            return "impossible"
        if (cx, cy) == (r, c) and c_cost == k:
            return direc
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if abs(nx-r) + abs(ny-c) + c_cost + 1 > k:
                continue
            if 0 < nx <= n and 0 < ny <= m:
                queue.append([nx, ny, c_cost+1, direc+direc_dict[i]])
                break
                
    return "impossible"
```    