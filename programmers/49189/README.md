### 프로그래머스 가장 먼 노드 (level 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/49189

### Algorithm: Dijkstra

```python
from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    conn = defaultdict(list)
    dist = [int(1e9)] * (n+1)
    dist[1] = 0
    
    for k, v in edge:
        conn[k].append(v)
        conn[v].append(k)
        
    dq = deque([(1, 0)])
    while dq:
        cpt, cost = dq.popleft()
        if dist[cpt] < cost:
            continue
        
        for nnode in conn[cpt]:
            if dist[nnode] > cost+1:
                dist[nnode] = cost+1
                dq.append((nnode, cost+1))
                
    dist = sorted(dist[1:])
    return len(list(filter(lambda x: x == max(dist), dist)))
```
