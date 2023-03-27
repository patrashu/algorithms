##  BOJ 1106 (G4)

### https://www.acmicpc.net/problem/1106

### Algorithm: DYnamic programmnig

Fail Code

``` python
import sys
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    c, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = sorted(a, key=lambda x:x[0])

    dp = [1e9] * (c+100)
    dp[0] = 0

    for cost, human in a:
        for i in range(human, c+100):
            dp[i] = min(dp[i-cost]+cost, dp[i])

    print(min(dp[c:]))    
```

