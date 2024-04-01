### 프로그래머스 다음 큰 숫자 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12911

### Algorithm: Implementation

```python
from collections import Counter

def solution(n):
    one = Counter(bin(n)[2:])["1"]
    
    while True:
        n += 1
        tmp = Counter(bin(n)[2:])["1"]
        if one == tmp:
            return n
```
