### 프로그래머스  '점찍기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/140107

### 구현


```python
def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        tmp = ((abs(d**2-i**2))**0.5)//k + 1
        answer += tmp
    return answer
```    