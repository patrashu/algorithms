# BOJ 14003 (P5)

## https://www.acmicpc.net/problem/14003
### Algorithm: BFS, Dynamic Programming, Binary Search


#### Fail code (will be modify) - Time Error
```python
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    visited = [0] * 1000001
    dp = [0] * 1000001
    visited[0] = 1
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and visited[j] + 1 > visited[i]:
                visited[i] = visited[j] + 1
                dp[i] = j
    idx = visited.index(max(visited))
    length = visited[idx]
    print(length)
    ans = []

    while length > 0:
        ans.append(a[idx])
        idx = dp[idx]
        length -= 1
    ans.reverse()
    print(' '.join(map(str, ans)))
```
