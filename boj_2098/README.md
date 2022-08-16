# BOJ 2098 (G1)

## https://www.acmicpc.net/problem/2098

### Algorithm: Dynamic programming, Bitmask, DFS

``` python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def dfs(x, y):
    if end == y:
        return a[x][0] if a[x][0] != 0 else float('inf')
    
    if dp[x][y] != 0:
        return dp[x][y]
    
    # set value inf
    cost = float('inf')
    
    # start searching
    for k in range(1, n):
        # if visited, skip
        if a[x][k] == 0 or y & (1<<k) > 0:
            continue
        
        # else calculate cost 
        cost = min(cost, a[x][k] + dfs(k, y | (1 << k)))
    
    # save min cost
    dp[x][y] = cost
    
    return cost


if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
        
    dp = [[0]*(1<<n) for _ in range(n)]
    end = (1<<n)-1
    
    print(dfs(0, 1))
    # print(dp)
```
