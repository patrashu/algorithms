### 프로그래머스 정수 삼각형 (level 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/43105

### Algorithm: DP

```python
def solution(triangle):
    length = len(triangle)
    dp = [[0]*length for _ in range(length)] 
    dp[0][0] = triangle[0][0]
    
    for i in range(1, length):
        for j in range(i+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    
    return max(dp[-1])
```
