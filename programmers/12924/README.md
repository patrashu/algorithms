### 프로그래머스 숫자 표현 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12924

### Algorithm: Implementation

```python
def solution(n):
    answer, idx, i = 0, 1, 1
    while idx <= n:
        i += 1
        idx += i
    
    for idx in range(1, i):
        if idx%2 == 1 and n%idx == 0:
            answer += 1
        elif idx%2 == 0 and (n+idx//2)%idx == 0:
            answer += 1
    
    return answer
```
