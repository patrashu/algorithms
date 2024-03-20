### 프로그래머스 '외벽 점검' (레벻 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/60062

### Algorithm: Implementation

```python
import copy
from collections import defaultdict, deque

def solution(n, weak, dist):
    answer = len(dist)+1
    dist.sort(key=lambda x: -x)
    fd = defaultdict(bool)
    for num in weak:
        fd[num] = False
    dq = deque([(0, fd)])
    
    while dq:
        depth, visited = dq.popleft()
        if depth >= answer:
            continue
        
        candits = []
        for num in weak:
            if not visited[num]:
                candits.append(num)
        
        for candit in candits:
            npts = []
            for i in range(dist[depth]+1):
                tmp = (candit+i)%n
                if tmp in visited:
                    npts.append(tmp)
                    
            nvisit = copy.deepcopy(visited)
            for npt in npts:
                nvisit[npt] = True
                
            if sum(nvisit.values()) == len(weak):
                answer = depth+1
                continue
            dq.append((depth+1, nvisit))
            
    return -1 if answer == len(dist)+1 else answer
```
