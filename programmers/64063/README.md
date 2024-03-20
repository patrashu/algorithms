### 프로그래머스 '호텔 방 배정' (레벨 4)

### https://school.programmers.co.kr/learn/courses/30/lessons/64063

### Algorithm: Union Find

```python
import sys
sys.setrecursionlimit(10**4)

def find_parent(table,x):
    if not table.get(x):
        table[x] = x + 1
        return x
    else:
        table[x] = find_parent(table,table[x])
        return table[x]

def solution(k, room_number):
    result = []
    table = dict()
    for room in room_number:
        result.append(find_parent(table,room))
        print(table)
    return result
```

``` python
from collections import deque, defaultdict

def solution(k, room_number):
    answer = []
    parent = defaultdict(int)
    
    for num in room_number:
        if not parent[num]:
            parent[num] = num+1
            answer.append(num)
        else:
            dq = deque()
            while parent[num] != 0:
                dq.append(num)
                num = parent[num]
            dq.append(num)            
            while dq:
                parent[dq.popleft()] = num+1
            answer.append(num)
    return answer
```