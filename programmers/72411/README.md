### 프로그래머스 2021 카카오 '메뉴 리뉴얼'(레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/72411

### Algorithm: Set, Combinations

```python
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for com in course:
        store = defaultdict(int)
        for order in orders:
            candits = combinations(order, com)
            
            for candit in candits:
                tmp = ''.join(sorted(candit))
                store[tmp] += 1
    
        store = sorted(store.items(), key=lambda x: -x[1])
        max_num = 0

        for menu, common in store:
            if common >= max_num and common != 1:
                max_num = common
                answer.append(menu)

    return sorted(answer)
```
