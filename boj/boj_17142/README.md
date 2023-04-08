##  BOJ 17142 (G3)

### https://www.acmicpc.net/problem/17142
### Algorithm: Combination, Implement, BFS

```python
import sys
from collections import deque
from itertools import combinations
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
field = []
viruses = []
total = 0
ans = 2501
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 바이러스 추출, 수용공간 추출
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            viruses.append((i, j))
    total += tmp.count(0)
    field.append(tmp)

if total == 0:
    print(0)
    sys.exit(0)

candits = combinations(viruses, m)
for cand in candits:
    # 활성 / 비활성
    for xx, yy in viruses:
        if (xx, yy) not in cand:
            field[xx][yy] = -3

    virus = deque(cand)
    # 맨 처음 virus
    visited = [[0]*n for _ in range(n)]
    tmp = total

    while virus:
        cx, cy = virus.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if field[nx][ny] == 0:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[cx][cy] + 1
                        virus.append((nx, ny))
                        tmp -= 1
                    elif visited[nx][ny] > visited[cx][cy] + 1:
                        visited[nx][ny] = visited[cx][cy] + 1
                        virus.append((nx, ny))
                elif tmp and field[nx][ny] == -3:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[cx][cy] + 1
                        virus.append((nx, ny))
                    elif visited[nx][ny] > visited[cx][cy] + 1:
                        visited[nx][ny] = visited[cx][cy] + 1
                        virus.append((nx, ny))

    # 활성 / 비활성
    for xx, yy in viruses:
        if (xx, yy) not in cand:
            field[xx][yy] = 2

    # 다 탐색하면 최대 시간 탐색
    if tmp == 0:
        cnt = 0
        for cc in visited:
            cnt = max(cnt, max(cc))
        ans = min(ans, cnt)

print(-1 if ans == 2501 else ans)
```