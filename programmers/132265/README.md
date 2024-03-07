### 프로그래머스  '롤케이크 자르기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/132265

### 구현


```python
from collections import defaultdict

def solution(topping):
    answer = 0
    test = defaultdict(int)
    for num in topping:
        test[num] += 1

    left = set()
    for num in topping:
        test[num] -= 1
        if test[num] == 0:
            del test[num]
        left.add(num)
        if len(left) == len(test):
            answer += 1
    return answer
```    