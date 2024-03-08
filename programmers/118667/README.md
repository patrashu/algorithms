### 프로그래머스  '두 큐 합 같게 만들기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/118687

### queue


```python
from collections import deque

def solution(queue1, queue2):
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    if (q1_sum+q2_sum) % 2 == 1:
        return -1
    
    queue1, queue2 = deque(queue1), deque(queue2)
    time = 0
    bound = len(queue1)*2+3
    while time < bound:
        if q1_sum == q2_sum:
            break
        
        if q1_sum < q2_sum:
            q1_sum += queue2[0]
            q2_sum -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            q2_sum += queue1[0]
            q1_sum -= queue1[0]
            queue2.append(queue1.popleft())
        time += 1
        
    return time if time < bound else -1
```    