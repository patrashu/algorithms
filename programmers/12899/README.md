### 프로그래머스 124 나라의 숫자 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12899

### Algorithm: Implementation

```python
def solution(n):
    result = ""
    while n > 0:
        n -= 1
        result = "124"[n%3] + result
        n //= 3
    return result
```
