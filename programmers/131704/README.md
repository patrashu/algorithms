### 프로그래머스  '택배상자' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/131704

### 구현


```python
def solution(order):
    answer = 1
    stack = list(range(1, order[0]))
    
    n_num = order[0]+1
    for i in range(1, len(order)):
        item = order[i]
        if not stack:
            answer, n_num = answer+1, n_num+1
            continue
        if item == stack[-1]:
            answer += 1
            stack.pop()
        elif item >= n_num:
            stack.extend(list(range(n_num, item)))
            answer += 1
            n_num = item+1
        else:
            break
    return answer
```    