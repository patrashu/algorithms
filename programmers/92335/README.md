### 프로그래머스 'k진수에서 소수 개수 구하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/92335

### Algorithm: Dict


```python
import math
from collections import defaultdict

def is_prime_number(x):
    if x == '' or x == '1':
        return False
    x = int(x)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def solution(n, k):
    # 나누기
    answer, conv = 0, ""
    while n > 0:
        q, v = divmod(n, k)
        conv += str(v)
        n = q
    
    for candit in conv[::-1].split("0"):
        if is_prime_number(candit):
            answer += 1
            
    return answer
```