### 프로그래머스 'N^2 배열 자르기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/87390

### Algorithm: Implementation


```python
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = i//n, i%n
        tmp = row if row > col else col
        answer.append(tmp+1)
        
    return answer
```