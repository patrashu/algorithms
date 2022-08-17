##  BOJ 19236 (G2)

### https://www.acmicpc.net/problem/19236
### Algorithm: Simulation, DFS, Implement


``` python
import sys
import copy
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
res = 0

def shuffle(sx, sy, score, a):
    global res
    score += a[sx][sy][0]
    res = max(res, score)
    a[sx][sy][0] = 0

    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if a[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        dist = a[f_x][f_y][1]

        for j in range(8):
            nd = (dist+j)%8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx==sx and ny==sy):
                continue

            a[f_x][f_y][1] = nd
            a[f_x][f_y], a[nx][ny] = a[nx][ny], a[f_x][f_y]
            break

    s_d = a[sx][sy][1]

    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and a[nx][ny][0] > 0:
            shuffle(nx, ny, score, copy.deepcopy(a))
    
    
if __name__ == '__main__':
    a = [[] for _ in range(4)]

    for i in range(4):
        line = list(map(int, input().split()))
        fish = []

        for j in range(0, 4):
            fish.append([line[j*2], line[j*2+1]-1])
        a[i] = fish

    shuffle(0, 0, 0, a)
    print(res) 
        
```


