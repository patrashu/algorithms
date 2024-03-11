### 프로그래머스 '튜플' (레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/64065

### Algorithm: DFS

```python
def solution(s):
    answer = []
    s = sorted(s[2:-2].split("},{"), key=len)
    visited = set()
    
    for i in s:
        sub = i.split(',')
        for ch in sub:
            if ch not in visited:
                visited.add(ch)
                answer.append(int(ch))
    return answer
```
