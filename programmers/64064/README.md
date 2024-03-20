### 프로그래머스 '불량 사용자' (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/64064

### Algorithm: Dfs

```python
from collections import defaultdict

def solution(user_id, banned_id):
    answer = set()
    bs = defaultdict(list)
    
    # preprocess
    for ban in banned_id:
        if len(bs[ban]) > 0: # if checked
            continue
        tmp = []
        for user in user_id:
            if len(user) != len(ban): # length diff
                continue
            flag = True
            for ch1, ch2 in zip(user, ban):
                if ch2 == '*':
                    continue
                if ch1 != ch2:
                    flag = False
                    break
            if flag:
                tmp.append(user)
        bs[ban] = tmp
    
    # dfs
    visited = set()
    def dfs(depth, direction):
        if depth == len(banned_id):
            answer.add(tuple(sorted(direction)))
            return
        
        for candit in bs[banned_id[depth]]:
            if candit not in visited:
                visited.add(candit)
                dfs(depth+1, direction + [candit])
                visited.discard(candit)
    dfs(0, [])
    return len(answer)
```