### 프로그래머스 압축 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/17684
### Algorithm: Implementation, dict

```python
def solution(msg):
    answer = []
    word = { chr(k): k-64 for k in range(65, 91)}
    sidx, eidx, nidx = 0, 0, 27
    
    while eidx < len(msg):
        while eidx < len(msg) and word.get(msg[sidx:eidx+1], -1) != -1:
            eidx += 1
        answer.append(word[msg[sidx:eidx]])
        word[msg[sidx:eidx+1]] = nidx
        nidx += 1
        sidx = eidx

    return answer
```
