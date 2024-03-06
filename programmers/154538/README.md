### 프로그래머스  '숫자 변환하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/154538

### BFS


```python
from collections import deque
def solution(x, y, n):
    answer = int(1e9)
    q = deque([(x, 0)])
    visited = [False] * (y+1)
    visited[x] = True
    
    while q:
        cpt, ccost = q.popleft()
        if cpt == y:
            answer = min(answer, ccost)
            continue
        
        for npt in [cpt+n, cpt*2, cpt*3]:
            if 0 <= npt <= y and not visited[npt]:
                visited[npt] = True
                q.append([npt, ccost+1])
            
    return -1 if answer == int(1e9) else answer
```    