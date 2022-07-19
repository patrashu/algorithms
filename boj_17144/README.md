##  BOJ 17144 (G4)

### https://www.acmicpc.net/problem/17144
### Algorithm: Simulation, Implement

```python
import sys
import copy
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline
def diffuse(j, k, div_dist):
    cnt = 0
    for i in range(4):
        nx = j + dx[i]
        ny = k + dy[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != -1:
            copy_a[nx][ny] += div_dist
            cnt += 1
    copy_a[j][k] -= cnt*div_dist
def up_rotate():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    up_x, up_y = air_fresh[0][0], 1
    direct = 0
    before = 0
    while direct < 4:
        nx = up_x + dx[direct]
        ny = up_y + dy[direct]
        if up_x == air_fresh[0][0] and up_y == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            direct += 1
            continue
        a[up_x][up_y], before = before, a[up_x][up_y]
        up_x = nx
        up_y = ny
def down_rotate():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    down_x, down_y = air_fresh[1][0], 1
    direct = 0
    before = 0
    while direct < 4:
        nx = down_x + dx[direct]
        ny = down_y + dy[direct]
        if down_x == air_fresh[1][0] and down_y == 0:
            break
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            direct += 1
            continue
        a[down_x][down_y], before = before, a[down_x][down_y]
        down_x = nx
        down_y = ny
if __name__ == '__main__':
    n, m, t = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    i, dist = 0, 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    air_fresh = []
    while i < t:
        copy_a = copy.deepcopy(a)
        ## Diffuse
        for j in range(n):
            for k in range(m):
                if a[j][k] == -1:
                    air_fresh.append((j, k))
                if a[j][k] > 4:
                    div_dist = a[j][k] // 5
                    diffuse(j, k, div_dist)
        a = copy_a
        i += 1
        up_rotate()
        down_rotate()
    for num in a:
        dist += sum(num)
    print(dist+2)
```