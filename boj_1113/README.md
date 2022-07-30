##  BOJ 1780 (G1)

### https://www.acmicpc.net/problem/1113
### Algorithm: DFS, BFS, Simulation


``` python
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def bfs(x, y, num):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    flag = True
    
    tmp = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = False
                continue
            
            if not visited[nx][ny] and a[nx][ny] <= num:
                visited[nx][ny] = 1
                queue.append([nx, ny])
                tmp += 1
    if flag:
        cnt += tmp
    else:
        return
                    

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for num in range(1, 10):
        visited = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j] <= num and not visited[i][j]:
                    bfs(i, j, num)
                    
    print(cnt)
```


