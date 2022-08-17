##  BOJ 16236 (G4)

### https://www.acmicpc.net/problem/16236
### Algorithm: Simulation, Implement, BFS

```python
import sys
sys.stdin = open('input.txt', 'rt')
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
shark_size = 2
shark_pos = None
eat = 0

def bfs(x, y, size):
    # make dist and visited list
    dist = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    # 
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = [] 
    
    while q:
        cur_x, cur_y = q.popleft()
        # search
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # check pos and visited
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                
                # check shark can go
                if field[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[cur_x][cur_y] + 1

                    # check shark can eat
                    if field[nx][ny] < size and field[nx][ny] != 0:
                        temp.append((nx, ny, dist[nx][ny]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


if __name__ == '__main__':
    n = int(input())
    field = []

    # input and save shark's pos
    for i in range(n):
        k = list(map(int, input().split()))
        for j in range(n):
            if k[j] == 9:
                shark_pos = [i, j]
        field.append(k)

    # result and cnt eat feeds
    res = 0 
    cnt = 0

    while True:
        shark = bfs(shark_pos[0], shark_pos[1], shark_size)

        # When empty list, break
        if not shark:
            break
        
        # calculate and change shark's pos
        nx, ny, dist = shark.pop()
        res += dist
        field[shark_pos[0]][shark_pos[1]], field[nx][ny] = 0, 0
        shark_pos = [nx, ny]

        # check eat feeds
        cnt += 1
        if cnt == shark_size:
            shark_size += 1
            cnt = 0

    print(res)
```