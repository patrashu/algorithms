### 프로그래머스  '우박수열 정적분' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/134239

### 구현


```python
def solution(k, ranges):
    answer = []
    integ = []
    while k > 1:
        nk = k*3+1 if k%2==1 else k//2
        min_y = min(nk, k)
        integ.append(min_y + abs(nk-k)/2)
        k = nk
        
    length = len(integ)
    for x1, x2 in ranges:
        x2 = length+x2
        if x1 == x2:
            answer.append(0)
        elif x2 < x1:
            answer.append(-1)
        else:
            answer.append(sum(integ[x1:x2]))
    
    return answer
```    