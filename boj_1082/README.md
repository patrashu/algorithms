##  BOJ 1082 (G3)

### https://www.acmicpc.net/problem/1082
### Algorithm: Dynamic Programming


``` python
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = dict()
    dp = [-1] * (m+1)
    dp[m] = 0

    for i in range(n):
        cnt[a[i]] = i

    for i in range(m, -1, -1):
        for j in range(n):
            if i-a[j] >= 0:
                if dp[i-a[j]] < dp[i]*10 + cnt[a[j]]:
                    dp[i-a[j]] = dp[i]*10 + cnt[a[j]]
        
    print(max(dp))

```


