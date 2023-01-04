## BOJ 18427 (G4)

### https://www.acmicpc.net/problem/18427

### Algorithm: Dynamic Programming

```python
import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
  n, m, h = map(int, input().split())
  blocks = [list(map(int, input().split())) for _ in range(n)]
  # add not using block case
  dp = [[1] + [0] * h for _ in range(n + 1)]

  for i in range(1, n+1):
    # copy formal table
    dp[i] = dp[i-1].copy()
    for block in blocks[i-1]:
      # add cases
      for j in range(block, h+1):
        dp[i][j] += dp[i-1][j-block]

  print(dp[n][h]%10007)
```
