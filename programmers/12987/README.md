### 프로그래머스 숫자 게임 (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/12987

### Algorithm: String

```python
import heapq

def solution(A, B):
    answer = 0
    q1, q2 = [-k for k in A], [-k for k in B]
    heapq.heapify(q1)
    heapq.heapify(q2)
    
    while q1:
        node1, node2 = heapq.heappop(q1), heapq.heappop(q2)
        if abs(node2) > abs(node1):
            answer += 1
            continue
        heapq.heappush(q2, node2)
    
    return answer
```
