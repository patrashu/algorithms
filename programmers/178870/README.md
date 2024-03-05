### 프로그래머스  '연속된 부분 수열의 합' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/178870

### 투 포인터


```python
def solution(sequence, k):
    length = len(sequence)
    i, j, sub = 0, 0, sequence[0]
    candit = []
    while j < length:
        if sub == k:
            candit.append((j-i, i, j))
            
        if sub >= k:
            sub -= sequence[i]
            i += 1
        else:
            if j == length-1:
                break
            else:
                j += 1
                sub += sequence[j]
    
    candit = sorted(candit, key=lambda x: x[0])[0]
    return candit[1:]
```    