### 프로그래머스 JadenCase 만들기 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12951

### Algorithm: String

```python
def solution(s):
    answer = []
    for ch in s.split(" "):
        tmp = ch.capitalize()
        answer.append(tmp)
    
    return ' '.join(answer)
```
