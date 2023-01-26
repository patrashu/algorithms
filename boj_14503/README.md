##  BOJ 14503 (G5)

### https://www.acmicpc.net/problem/14503
### Algorithm: Implementation, Simulation

```python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dist = None
rot_cnt = 0


def turn_left():
    global dist
    dist -= 1
    if dist == -1:
        dist = 3


if __name__ == '__main__':
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    cnt, dist = 1, d

    while True:
        # search start
        turn_left()
        nx = r + dx[dist]
        ny = c + dy[dist]

        # not clean and not visited
        if visited[nx][ny] == 0 and field[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            r, c = nx, ny
            rot_cnt = 0
            continue

        # clean area
        else:
            rot_cnt += 1

        # all clean
        if rot_cnt == 4:
            # go back
            nx = r - dx[dist]
            ny = c - dy[dist]

            # check wall
            if field[nx][ny] == 0:
                r, c = nx, ny
            else:
                break

            rot_cnt = 0

    print(cnt)
```
- 전형적인 시뮬레이션 구현 문제
- 조건에 맞게 코드작성만 잘하면 됨.