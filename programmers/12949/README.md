### 프로그래머스 행렬의 곱셈 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/12949

### Algorithm: Math

```python
def rot90(arr):
    return [list(matrix) for matrix in zip(*arr)]

def solution(arr1, arr2):
    r, c = len(arr1), len(arr2[0])
    new_arr = [[0]*c for _ in range(r)]
    arr2 = rot90(arr2)
    
    for i in range(r):
        for j in range(c):
            tmp = sum([k*v for k, v in zip(arr1[i], arr2[j])])
            new_arr[i][j] = tmp
            
    return new_arr
```

```python
import numpy as np

def solution(arr1, arr2):
    return np.matmul(arr1, arr2).tolist()
```