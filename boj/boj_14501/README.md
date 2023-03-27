##  BOJ 16236 (S3)

### https://www.acmicpc.net/problem/14501
### Algorithm: DP


### BruteForce
```python
import sys
input = sys.stdin.readline


if __name__ == '__main__':
  n = int(input())
  schedules = [list(map(int, input().split())) for _ in range(n)]
  dp = [0]*(n+1)

  for i in range(n-1, -1, -1):
    if schedules[i][0] + i > n:
      dp[i] = dp[i+1]
    else:
      dp[i] = max(dp[i+1], dp[i+schedules[i][0]] + schedules[i][1])

  print(dp[0])
```