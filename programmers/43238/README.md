### 프로그래머스 입국심사 (level 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/43238

### Algorithm: Binary Search

```python
def solution(n, times):
    l, r = min(times), 1e18
    while l <= r:
        mid = (l+r) // 2
        cnt = sum([mid//k for k in times])   
        if cnt >= n:
            r = mid -1
        else:
            l = mid + 1
    
    return l
```
