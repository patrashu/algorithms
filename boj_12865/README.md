# BOJ 12865 (G5)

## https://www.acmicpc.net/problem/12865
### Algorithm: Knapsack, Dynamic Programming

``` python
import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
  n, k = map(int, input().split())
  bags = [list(map(int, input().split())) for _ in range(n)]

  dp = [[0] * (k + 1) for _ in range(n + 1)]
  for i in range(1, n + 1):
    tmp = bags[i-1]
    for j in range(1, k + 1):
      if j < tmp[0]:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tmp[0]] + tmp[1])

  print(dp)
  print(dp[n][k])
```