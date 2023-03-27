## BOJ 11404 (G4)

### https://www.acmicpc.net/problem/11404

### Algorithm: Floyd wassal

```python
import sys
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = [[int(1e9)]*n for _ in range(n)]

    for _ in range(m):
        p, q, cost = map(int, input().split())
        a[p-1][q-1] = min(a[p-1][q-1], cost)


    for k in range(n):
        a[k][k] = 0
        for i in range(n):
            for j in range(n):
                if a[i][j] != 0 and a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]


    for i in range(n):
        for j in range(n):
            print(a[i][j] if a[i][j] != int(1e9) else 0, end = ' ')
        print()
```
