##  BOJ 19238 (G2)

### https://www.acmicpc.net/problem/19238
### Algorithm: Implementation, BFS


``` python
import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    n, m, fuel = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    sx, sy = map(int, input().split())
    sx, sy = sx-1, sy-1
    person = [list(map(int, input().split())) for _ in range(m)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    c_person = dict()
    for stx, sty, ex, ey in person:
        c_person[(stx - 1, sty - 1)] = (ex - 1, ey - 1)

    while len(person) > 0:
        q = deque([(sx, sy, 0)])
        cnt = len(c_person.keys())
        visited = [[0]*n for _ in range(n)]
        visited[sx][sy] = 1
        level = 400
        candit = []

        # 손님을 다 태웠을때를 고려
        while cnt and q:
           cx, cy, cost = q.popleft()
           # 동일 레벨에 있는걸 먼저
           if cost <= level:
               if (cx, cy) in c_person:
                   candit.append([cost, cx, cy, c_person[(cx, cy)]])
                   level = cost
                   cnt -= 1

               for i in range(4):
                   nx, ny = cx + dx[i], cy + dy[i]
                   # 범위 안 + 벽 x + 방문 x => 탐색 ㄱ
                   if 0 <= nx < n and 0 <= ny < n and field[nx][ny] != 1 and not visited[nx][ny]:
                       visited[nx][ny] = 1
                       q.append((nx, ny, cost+1))
           else:
               continue

        # 승객을 태울 수 있는지 판단
        if candit:
            # candit에서 정렬 후 하나씩
            candit = sorted(candit, key=lambda x: (x[0], x[1], x[2]))
            n_cand = candit[0]
            eq = deque([(n_cand[1], n_cand[2], 0)])
            e_dist, flag = 0, False
            e_visited = [[0]*n for _ in range(n)]
            e_visited[n_cand[1]][n_cand[2]] = 1

            while eq:
                cx, cy, cost = eq.popleft()
                if (cx, cy) == n_cand[3]:
                    e_dist = cost
                    flag = True
                    break

                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and field[nx][ny] != 1 and not e_visited[nx][ny]:
                        e_visited[nx][ny] = 1
                        eq.append((nx, ny, cost + 1))

            if flag:
                if fuel - e_dist - n_cand[0] < 0:
                    fuel = -1
                    break
                else:
                    del c_person[(n_cand[1], n_cand[2])]
                    sx, sy = n_cand[3]
                    fuel = fuel - n_cand[0] + e_dist
            else:
                fuel = -1
                break
        else:
            break

    if len(c_person) > 0:
        print(-1)
    else:
        print(fuel)
```