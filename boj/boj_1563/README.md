##  BOJ 1563 (G4)

### https://www.acmicpc.net/problem/1563
### Algorithm: DFS, DP


``` python
import sys
sys.stdin = open("input.txt", "rt")

def main(n: int) -> int:
  dp = [[0]*3 for _ in range(n+1)]
  dp[1] = [1, 1, 1]
  dp[2] = [3, 2, 3]
  dp[3] = [8, 4, 7]

  for i in range(4, n+1):
    new_row = [0]*3
    for j in range(3):
      if j == 0:
        new_row[j] = sum(dp[i-1])
      elif j == 1:
        formal = dp[i-2][j-1] + dp[i-2][j+1] - 2*dp[i-3][j]
        new_row[j] = dp[i-1][j-1] + dp[i-1][j+1] - 2*formal
      else:
        new_row[j] = sum(dp[i-1]) - 2*dp[i-3][j]

    dp[i] = new_row

  return sum(dp[-1])


if __name__ == '__main__':
  n = int(input())
  print(main(n))
```

``` python
n = 1000
mod = 1000000
dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
dp[1][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1
for N in range(1, n):
    dp[N+1][0][0] = (dp[N][0][0] + dp[N][0][1] + dp[N][0][2])%mod
    dp[N+1][0][1] = dp[N][0][0]
    dp[N+1][0][2] = dp[N][0][1]
    dp[N+1][1][0] = (dp[N][1][0] + dp[N][1][1] + dp[N][1][2] +
                     dp[N][0][0] + dp[N][0][1] + dp[N][0][2])%mod
    dp[N+1][1][1] = dp[N][1][0]
    dp[N+1][1][2] = dp[N][1][1]

n = int(input())
print((DP[n][1][0] + DP[n][1][1] + DP[n][1][2] + DP[n][0][0] + DP[n][0][1] + DP[n][0][2])%mod)
```


