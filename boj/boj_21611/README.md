##  BOJ 21611 (G1)

### https://www.acmicpc.net/problem/21611
### Algorithm: Implementation, Simulation


``` python
import sys
from collections import defaultdict
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
balls = [list(map(int, input().split())) for _ in range(m)]
sx, sy = n//2, n//2
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def snake():
    cx, cy = sx, sy
    i, j = 1, 1
    n_list = []
    while True:
        if len(n_list) == n**2:
            break

        go = (i+j)//2
        if i % 2 == 1 and j % 2 == 1:
            for p in range(cy-1, cy-1-go, -1):
                n_list.append((cx, p))
                cy = p
            i += 1
        elif i % 2 == 0 and j % 2 == 1:
            for p in range(cx+1, cx+go+1):
                n_list.append((p, cy))
                cx = p
            j += 1
        elif i % 2 == 0 and j % 2 == 0:
            for p in range(cy+1, cy+go+1):
                n_list.append((cx, p))
                cy = p
            i += 1
        elif i % 2 == 1 and j % 2 == 0:
            for p in range(cx-1, cx-1-go, -1):
                n_list.append((p, cy))
                cx = p
            j += 1
    return n_list


def find_blocks():
    i = 0
    st, et = 0, 0
    cnt = 0
    value = 0
    blocks = []
    while i < len(snakes):
        cx, cy = snakes[i]
        if value != field[cx][cy]:
            if cnt >= 4:
                blocks.append([value, snakes[st:et + 1]])
            value = field[cx][cy]
            cnt = 1
            st, et = i, i
        else:
            cnt += 1
            et += 1
        i += 1

    # 남은거 블록 처리
    if cnt >= 4:
        blocks.append([value, snakes[st:et + 1]])

    return blocks


all_pts = snake()
marbles = defaultdict(int)
for dist, cost in balls:
    zeros = 0
    for i in range(n):
        zeros += field[i].count(0)
    snakes = all_pts[:n ** 2 - zeros]

    # 일단 부숴
    for i in range(cost):
        nx, ny = sx + dx[dist]*(i+1), sy + dy[dist]*(i+1)
        if field[nx][ny]:
            field[nx][ny] = 0
            snakes.pop(snakes.index((nx, ny)))

    # 인덱스, 연속되는 블록 찾기, 연속 처리
    while True:
        blocks = find_blocks()
        if not blocks:
            break

        # 블록 추출하고 0으로 처리
        for block in blocks:
            for xx, yy in block[1]:
                snakes.pop(snakes.index((xx, yy)))
                field[xx][yy] = 0
            marbles[block[0]] += len(block[1])

    if snakes:
        i, j = 0, 0
        n_value = None
        n_field = [[0]*n for _ in range(n)]
        while i < n**2 and j < len(snakes):
            st, et = j, j
            value = field[snakes[j][0]][snakes[j][1]]

            while True:
                nx, ny = snakes[j]
                if value == field[nx][ny]:
                    j += 1
                    et += 1
                # 다르면
                else:
                    n_value = value
                    break
                # 맨 끝이면
                if j == len(snakes):
                    n_value = value
                    break

            cnt = et - st
            if i + 2 < n**2:
                nx, ny = all_pts[i]
                nnx, nny = all_pts[i+1]
                n_field[nx][ny] = cnt
                n_field[nnx][nny] = n_value
                i += 2
            elif i + 1 < n**2:
                nx, ny = all_pts[i]
                n_field[nx][ny] = cnt
                break
        field = n_field
    else:
        break


ans = 0
for i in range(1, 4):
    ans += marbles[i]*i

print(ans)
```