### 프로그래머스 '풍선 터트리기' (레벻 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/68646

### Algorithm: Implementation

```python
def solution(a):
    def input_min(k):
        q = []
        t = k[0]
        for x in k:
            if t > x:
                t = x
            q.append(t)
        return q
    k = set(input_min(a) + input_min(list(reversed(a))))

    return len(k)
```
