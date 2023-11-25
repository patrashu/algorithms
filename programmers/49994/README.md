### 프로그래머스 49994번

### https://school.programmers.co.kr/learn/courses/30/lessons/49994

### Algorithm: Dict, Simulation

```python
from collections import deque, defaultdict

def solution(dirs):
    visited = defaultdict(bool)
    direc = {
        'L': (0, -1), 'R': (0, 1), 'U': (1, 0), 'D': (-1, 0)
    }
    
    cx, cy = 0, 0
    for ndir in dirs:
        try:
            dx, dy = direc[ndir]
            nx, ny = cx+dx, cy+dy
            if nx < -5 or nx > 5 or ny < -5 or ny > 5:
                raise ValueError ("asd")
            
            if visited[(cx, cy, nx, ny)] is True or visited[(nx, ny, cx, cy)] is True:
                cx, cy = nx, ny
                continue
                
            visited[(cx, cy, nx, ny)] = True
            visited[(nx, ny, cx, cy)] = True
            cx, cy = nx, ny
        except:
            pass
    
    return len(list(filter(lambda x: x[1] == True, visited.items()))) // 2
```
