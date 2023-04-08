##  BOJ 17143 (G1)

### https://www.acmicpc.net/problem/17143
### Algorithm: Simulation, Implementation

```python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

r, c, m = map(int, input().split())
field = [[[] for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
px = 0
eats = 0

for _ in range(m):
    sx, sy, cost, dd, size = map(int, input().split())
    field[sx-1][sy-1] = [size, cost, dd-1]

while px < c:
    # 이동 후 낚시
    for i in range(r):
        if len(field[i][px]) != 0:
            eats += field[i][px][0]
            field[i][px] = []
            break

    n_field = [[[] for _ in range(c)] for _ in range(r)]
    # 상어들 이동
    for i in range(r):
        for j in range(c):
            # 상어가 있으면
            if field[i][j]:
                cx, cy = i, j
                size, cost, dd = field[i][j]
                ccost = cost
                # 움직이는건 똑같으니까
                if dd in [0, 1]:
                    cost %= (2*r-2)
                    while cost > 0:
                        nx, ny = cx + dx[dd], cy + dy[dd]
                        if 0 <= nx < r:
                            cost -= 1
                            cx, cy = nx, ny
                            continue
                        elif nx == -1:
                            dd = 1
                        elif nx == r:
                            dd = 0
                    if not n_field[cx][cy]:
                        n_field[cx][cy] = [size, ccost, dd]
                    elif n_field[cx][cy] and n_field[cx][cy][0] < size:
                        n_field[cx][cy] = [size, ccost, dd]
                else:
                    cost %= (2*c-2)
                    while cost > 0:
                        nx, ny = cx + dx[dd], cy + dy[dd]
                        if 0 <= ny < c:
                            cost -= 1
                            cx, cy = nx, ny
                            continue
                        elif ny == -1:
                            dd = 2
                        elif ny == c:
                            dd = 3

                    if not n_field[cx][cy]:
                        n_field[cx][cy] = [size, ccost, dd]
                    elif n_field[cx][cy] and n_field[cx][cy][0] < size:
                        n_field[cx][cy] = [size, ccost, dd]

    field = n_field
    px += 1

print(eats)
```