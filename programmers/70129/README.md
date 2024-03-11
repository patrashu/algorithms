### 프로그래머스 '이진 변환 반복하기'(레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/70129

### Algorithm: Implementation

```python
def solution(s):
    answer = [0, 0]
    
    while s != '1':
        ns = ''.join(s.split("0"))
        answer[0] += 1
        answer[1] += (len(s)-len(ns))
        s = str(bin(len(ns))[2:])
    
    return answer
```
