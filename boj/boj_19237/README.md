##  BOJ 19237 (G2)

### https://www.acmicpc.net/problem/19237
### Algorithm: Simulation, BFS, Implementation


``` python
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 상어 초기 위치 추출
n, m, k = map(int, input().split())
sharks = [[0, 0] for _ in range(m+1)]
cnt_shark = m
field = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] > 0:
            sharks[tmp[j]] = [i, j]
    field.append(tmp)

# 방향 저장
dirs = [0] + list(map(int, input().split()))
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 우선순위 저장
prior = dict()
for i in range(m):
    tmp = [[],]
    for j in range(4):
        pp = list(map(int, input().split()))
        tmp.append(pp)

    prior[i+1] = tmp

# 냄새 저장 => 3차원 초기화
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
for i in range(1, m+1):
    smell[sharks[i][0]][sharks[i][1]] = [i, k]

time = 0
while True:
    queue = deque()
    # 상어별로 이동 시작
    for i in range(1, m+1):
        cx, cy = sharks[i]
        # 잡아먹힌 상어라면
        if cx == -1 and cy == -1:
            continue

        # 4방향 탐색 및 자신 냄새 확인
        tmp_s, flag = [], True
        for j in prior[i][dirs[i]]:
            nx, ny = cx + dx[j], cy + dy[j]
            if 0 <= nx < n and 0 <= ny < n:
                # 비어있는 곳이라면
                # 현재점 5로 세팅,
                if smell[nx][ny][0] == 0:
                    # 맨 처음 상어랑 동일 위치면
                    queue.append((i, j, nx, ny))
                    flag = False
                    break

                # 냄새가 있어
                else:
                    if smell[nx][ny][0] == i:
                        tmp_s.append((nx, ny, j))

        # 꽉차있고 냄새로 이동하는 경우
        # 시작점 최신화, 방향 최신화
        if flag and tmp_s:
            nt = tmp_s[0]
            sharks[i] = [nt[0], nt[1]]
            smell[nt[0]][nt[1]] = [i, k+1]
            dirs[i] = nt[2]

    while queue:
        i, dist, nx, ny = queue.pop()
        if smell[nx][ny][0] == 0:
            smell[nx][ny] = [i, k+1]
            sharks[i] = [nx, ny]
            dirs[i] = dist
        else:
            c_idx = smell[nx][ny][0]
            sharks[c_idx] = [-1, -1]
            smell[nx][ny] = [i, k+1]
            sharks[i] = [nx, ny]
            dirs[i] = dist
            cnt_shark -= 1

    # 1씩 감소
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = [0, 0]

    time += 1
    # 탈출 조건
    if time == 1000:
        if cnt_shark > 1:
            time = -1
            break

    if cnt_shark == 1:
        break

print(time)
```