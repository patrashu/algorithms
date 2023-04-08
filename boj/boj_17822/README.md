##  BOJ 17822 (G2)

### https://www.acmicpc.net/problem/17822

### Algorithm: Implementation, BFS


``` python
import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
field = [deque(list(map(int, input().split()))) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(t)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
remains = n*m
cur = 0


def bfs(x, y, visited):
    global blocks, cur
    q = deque([(x, y)])
    visited[x][y] = 1
    uptwo = [(x, y)]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = (cy + dy[i]) % m
            # 범위 안에이면서 value가 같고 방문을 안한경우
            if 0 <= nx < n and not visited[nx][ny]:
                if field[nx][ny] == field[x][y]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    uptwo.append((nx, ny))

    # 연속 블록이 없는 경우
    if len(uptwo) == 1:
        blocks += 1
    else:
        for xx, yy in uptwo:
            field[xx][yy] = 0
            cur += 1
    return visited


for order in orders:
    num, dist, cost = order
    for i in range(num-1, n, num):
        # 시계 방향 / 반시계 방향
        if dist == 0: field[i].rotate(cost)
        else: field[i].rotate(-cost)

    visited = [[0]*m for _ in range(n)]
    blocks = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] > 0:
                visited = bfs(i, j, visited)

    if blocks != 0 and blocks == remains:
        avg = 0
        for i in range(n):
            for j in range(m):
                if field[i][j]:
                    avg += field[i][j]

        avg /= remains
        for i in range(n):
            for j in range(m):
                if field[i][j] > avg:
                    field[i][j] -= 1
                elif field[i][j] != 0 and field[i][j] < avg:
                    field[i][j] += 1
    else:
        remains -= cur
        cur = 0

ans = 0
for cc in field:
    ans += sum(cc)
print(ans)
```