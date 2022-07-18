##  BOJ 10830 (G4)

### https://www.acmicpc.net/problem/10830
### Algorithm: Div and Conquer

```python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def cal_mat(mat1, mat2):
    global n
    res_mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_mat[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return res_mat


def div_and_conquer(a, m):
    if m == 1:
        return a
    else:
        sub_mul = div_and_conquer(a, m//2)
        if m % 2 == 0:
            return cal_mat(sub_mul, sub_mul)
        else:
            return cal_mat(cal_mat(sub_mul, sub_mul), a)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    result = div_and_conquer(a, m)

    for i in range(n):
        for j in range(n):
            print(result[i][j] % 1000, end=' ')
        print()

```

#### 비슷한 유형
https://www.acmicpc.net/problem/1780
