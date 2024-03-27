### 프로그래머스 야근 지수 (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/12927

### Algorithm: Heapq

```python
import heapq

def solution(n, works):
    works = [-k for k in works]
    heapq.heapify(works)
    
    while works and n:
        cpt = heapq.heappop(works)
        if cpt < -1:
            heapq.heappush(works, cpt+1)
        n -= 1
    
    answer = sum([k**2 for k in works])
    return answer
```
