### 프로그래머스  '디펜스 게임' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/142085

### 우선순위 큐, 구현


```python
import heapq

def solution(n, k, enemy):
    answer = 0
    q = []
    length = len(enemy)
    for i in range(length):
        if k:
            heapq.heappush(q, enemy[i])
            k -= 1
            answer += 1
            continue
        
        # 교체 가능할 때 
        root_node = heapq.heappop(q)
        if root_node < enemy[i]:
            heapq.heappush(q, enemy[i])
            if n - root_node < 0:
                break
            n -= root_node
            answer += 1
            
        # 불가능할 때
        else:
            heapq.heappush(q, root_node)
            if n - enemy[i] < 0:
                break
            n -= enemy[i]
            answer += 1
        
    
    return answer

```    