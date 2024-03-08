### 프로그래머스  '할인 행사' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/131127

### 구현


```python
from collections import defaultdict, Counter

def solution(want, number, discount):
    answer = 0
    
    want = { k:v for k, v in zip(want, number) }
    data = Counter(discount[:10])
    
    for i in range(len(discount)-10):
        if want == data:
            answer += 1
            
        data[discount[i]] -= 1
        data[discount[i+10]] += 1
        if data[discount[i]] == 0:
            del data[discount[i]]

    return answer+1 if want == data else answer
```    