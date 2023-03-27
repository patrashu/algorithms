##  BOJ 1103 (G2)

### https://www.acmicpc.net/problem/1103
### Algorithm: Dynamic Programming, DFS, Set


``` python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):

    for i in range(4):
        k = a[x][y]
        nx = x + dx[i]*int(k)
        ny = y + dy[i]*int(k)

        if nx < 0 or nx >= n or ny < 0 or ny >= m or a[nx][ny] == 'H':
            continue
        
        if dp[x][y] + 1 > dp[nx][ny]:
            if (nx, ny) in visited:     
                print(-1)
                sys.exit(0)
            else:
                visited.add((nx, ny))
                dp[nx][ny] = dp[x][y] + 1
                dfs(nx, ny)
                visited.remove((nx, ny))


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(input().strip()) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    visited = set()

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dp[0][0] = 1
    visited.add((0, 0))
    dfs(0, 0)

    max_num = 0
    for num in dp:
        max_num = max(max_num, max(num))

    print(max_num)
```


