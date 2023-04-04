##  BOJ 17144 (G4)

### https://www.acmicpc.net/problem/17144
### Algorithm: Simulation, Implement

```python
import sys
import copy
input = sys.stdin.readline

def wind(n_field, airs):
    up = airs[0]
    down = airs[1]

    corner = 0
    ndx = [0, -1, 0, 1]
    ndy = [-1, 0, 1, 0]
    cx, cy = up

    while True:
        idx = corner%4
        nx, ny = cx + ndx[idx], cy + ndy[idx]
        if nx < 0 or nx > up[0] or ny < 0 or ny >= c:
            corner += 1
            continue
        if (nx, ny) == up:
            break

        n_field[cx][cy] = n_field[nx][ny]
        cx, cy = nx, ny

    corner = 0
    ndx = [0, 1, 0, -1]
    ndy = [-1, 0, 1, 0]
    cx, cy = down

    while True:
        idx = corner%4
        nx, ny = cx + ndx[idx], cy + ndy[idx]
        if nx < down[0] or nx >= r or ny < 0 or ny >= c:
            corner += 1
            continue
        if (nx, ny) == down:
            break

        n_field[cx][cy] = n_field[nx][ny]
        cx, cy = nx, ny

    n_field[up[0]][up[1]] = -1
    n_field[down[0]][down[1]] = -1
    if up[1] < c-1:
        n_field[up[0]][up[1]+1] = 0
    if down[1] < c-1:
        n_field[down[0]][down[1] + 1] = 0

    return n_field


if __name__ == '__main__':
    r, c, t = map(int, input().split())
    field = []
    airs = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 시작점 찾기
    for i in range(r):
        tmp = list(map(int, input().split()))
        for j in range(c):
            if tmp[j] == -1:
                airs.append((i, j))
        field.append(tmp)

    time = 0
    while time < t:
        n_field = copy.deepcopy(field)
        for i in range(r):
            for j in range(c):
                if field[i][j] != -1 and field[i][j] != 0:
                    cnt = 0
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < r and 0 <= ny < c and field[nx][ny] != -1:
                            cnt += 1
                            n_field[nx][ny] += field[i][j] // 5
                    n_field[i][j] -= cnt * (field[i][j] // 5)

        n_field = wind(n_field, airs)
        field = n_field
        time += 1

    ans = 0
    for cc in field:
        ans += sum(cc)

    print(ans + 2)

```