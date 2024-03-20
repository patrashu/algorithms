### 프로그래머스 '징검다리 건너기' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/64062

### Algorithm: Binary Search, Sliding Window Maximum

```python
def solution(stones, k):
    l, r = 1, 200000000
    while l <= r:
        mid = (l+r) // 2
        cnt, flag = 0, True
        for num in stones:
            if num-mid < 0:
                cnt += 1
                if cnt >= k:
                    flag = False
                    break
            else:
                cnt = 0
        # 몬가면
        if not flag:
            r = mid - 1
        else:
            # answer = mid
            l = mid + 1
    return r
```

``` python
from collections import deque

def solution(stones, k):
    dq = deque() 
    ans = []
    
    # 첫번째 슬라이딩 윈도우 중 최대값의 idx를 추가
    for i in range(k):
        while dq and stones[dq[-1]] < stones[i]:
            dq.pop()
        dq.append(i)
    
    ans.append(stones[dq[0]])
    for i in range(k, len(stones)):
        # 첫 번째 idx가 i와 일치하면 사라지는 부분
        if i == dq[0]+k:
            dq.popleft()
            
        while dq and stones[dq[-1]] < stones[i]:
            dq.pop()
        
        dq.append(i)
        ans.append(stones[dq[0]])
    return min(ans)
```