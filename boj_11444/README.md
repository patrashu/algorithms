# BOJ 11444 (G2)

## https://www.acmicpc.net/problem/11444

### Algorithm: Divide and conquer
 
1. n이 너무 크기 때문에 재귀나 DP로 해결 불가능
2. 분할 정복을 활용하여 O(log n)으로 해결
3. 선형 대수학 기본 지식(행렬 곱셈) 활용

![image](https://user-images.githubusercontent.com/78347296/178130938-f071bfa5-b225-4c83-ba58-b88b8fab4381.png)


``` python
import sys
from typing import List, Tuple
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def multi(
    mat1: List[List[int]],
    mat2: List[List[int]]
) -> List[List[int]]:

    global div
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j] % div
    
    return res


def div_and_conquer(
    a: List[List[int]],
    b: int
) -> List[List[int]]:

    if b == 1:
        return a
    else:
        tmp = div_and_conquer(a, b // 2)
        if b % 2 == 0:
            return multi(tmp, tmp)
        else:
            return multi(multi(tmp, tmp), a)


if __name__ == '__main__':
    n = int(input())
    div = 1000000007
    matrix = [[1, 1], [1, 0]]
    
    result = div_and_conquer(matrix, n)
    
    print(result[0][1] % div) 
```
