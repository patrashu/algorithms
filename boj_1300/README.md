## BOJ 1300 (G2)

### https://www.acmicpc.net/problem/1300

### Algorithm: Binary search

```python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    low, high = 0, M+1
    ans = 0

    while low <= high:
        mid = (low+high)//2

        cnt = 0
        for i in range(1, N+1):
            cnt = cnt + min(mid//i, N)

        if cnt < M:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1

    print(ans)
```
