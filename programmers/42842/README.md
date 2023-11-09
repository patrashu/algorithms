### 프로그래머스 카펫 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/42842

### Algorithm: Implementation, math

```python
def solution(brown, yellow):
    """
    둘레 = 2(r+c-1)
    너비 = r*c => brown+yellow
    
    """
    area = brown+yellow
    for i in range(1, area//2+1):
        if area % i == 0:
            j = area // i
            if 2*(i+j-2) == brown:
                return [j, i]
    return answer
```
