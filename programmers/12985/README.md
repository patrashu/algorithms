### 프로그래머스 예상 대진표 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12985

### Algorithm: String

```python
def solution(n,a,b):
    answer = 1
    if a > b: a, b = b, a
    
    while True:
        if b%2 == 0 and (b-a) == 1:
            break
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer
```
