### 프로그래머스 2021 카카오 '메뉴 리뉴얼'(레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/72411

### Algorithm: Set, Combinations

```python
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    res = []
    for num in course:
        store = defaultdict(int)
        for order in orders:
            candidates = combinations(order, num)

            for candidate in candidates:
                tmp = ''.join(sorted(candidate))
                store[tmp] += 1

        store = sorted(store.items(), key=lambda x: -x[1])
        max_num = 0

        for menu, common in store:
            if common >= max_num and common != 1:
                max_num = common
                res.append(menu)

    return sorted(res)
```
