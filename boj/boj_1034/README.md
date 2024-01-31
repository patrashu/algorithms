##  BOJ 1034 (G4)

### https://www.acmicpc.net/problem/1034

### Algorithm: Bruteforce


``` python
import sys
from collections import defaultdict


def main(n: int, m: int, field: list[int], k: int):
    col_dict = defaultdict(int)
    for row in range(n):
        idxs = [i for i, value in enumerate(field[row]) if value == 0]
        col_dict[tuple(idxs)] += 1

    col_list = list(filter(lambda x: len(x[0]) <= k, col_dict.items()))
    col_list = list(filter(lambda x: len(x[0])%2 == k%2, col_list))
    try:
        answer = sorted(col_list, key=lambda x: -x[1])[0][1]
    except:
        answer = 0
    print(answer)


if __name__ == '__main__':
  n, m = map(int, input().split())
  field = [list(map(int, input())) for _ in range(n)]
  k = int(input())
  main(n, m, field, k)
```