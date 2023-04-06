##  BOJ 21609 (G2)

### https://www.acmicpc.net/problem/21609
### Algorithm: Implementation, BFS


``` python
import copy
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def extract_blocks():
    blocks = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 방문 했거나, field[i][j]가 1보다 작은 경우 (무지개 아니면서 일반 노드일 때)
            if visited[i][j] or field[i][j] <= 0:
                continue
            visited[i][j] = 1
            bcnt, zcnt, pts, visited = bfs(i, j, field[i][j], visited)
            if bcnt >= 2:
                blocks.append([bcnt, zcnt, i, j, pts])

    return blocks

def bfs(x, y, node, visited):
    q = deque([(x, y)])
    pts = [(x, y)]
    zero = []
    bcnt, zcnt = 1, 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if field[nx][ny] == node:
                visited[nx][ny] = 1
                q.append((nx, ny))
                bcnt += 1
                pts.append((nx, ny))

            elif field[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                bcnt += 1
                zero.append((nx, ny))
                zcnt += 1

    for xx, yy in zero:
        visited[xx][yy] = 0

    return [bcnt, zcnt, pts+zero, visited]


def rotate(field):
    new_field = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_field[j][i] = field[i][n-1-j]

    return new_field


def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if field[i][j] != -1:
                tmp = i
                while tmp + 1 < n and field[tmp+1][j] == -2:
                    field[tmp+1][j] = field[tmp][j]
                    field[tmp][j] = -2
                    tmp += 1


ans = 0
# 추출해서 sort
while True:
    blocks = extract_blocks()
    blocks = sorted(blocks, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

    if not blocks:
        break
    block = blocks[0]
    ans += block[0] ** 2
    for xx, yy in block[4]:
        field[xx][yy] = -2

    # break
    gravity()
    field = rotate(field)
    gravity()

print(ans)
```