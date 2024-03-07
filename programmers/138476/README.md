### 프로그래머스  '귤 고르기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/138476

### 구현


```python
"""
K개를 고를 때 종류를 최소로
=> Counter -> sort -> cnt
"""
from collections import Counter

def solution(k, tangerine):
    answer = 0
    tan = sorted(Counter(tangerine).items(), key=lambda x: -x[1])
    for key, value in tan:
        k -= value
        answer += 1
        if k <= 0:
            break
    
    return answer
```    