### 프로그래머스  '디펜스 게임' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/142085

### 우선순위 큐, 구현


```python
from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap) 
            k -= 1
        answer += 1
    return answer
```    