##  BOJ 23291 (P5)

### https://www.acmicpc.net/problem/23291
### Algorithm: Implementation, Simulation


``` python
def rotate_90_right(arr):
    return [list(reversed(col)) for col in zip(*arr)]


n, k = map(int, input().split())
field = list(map(int, input().split()))
time = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # min value + 1
    field = list(map(lambda x: x+1 if x == min(field) else x, field))

    # find upper case
    upper = [field[0]]
    idx = 1
    r, c = 1, 1
    while idx < n:
        if idx == 1:
            upper = [[upper[0]], [field[idx]]]
            idx += r
            r, c = c+1, r
        elif idx + r-1 < n:
            upper = rotate_90_right(upper)
            upper.append(field[idx: idx + r])
            idx += r
            r, c = c+1, r
        else:
            break

    # make new field
    col = idx-c if idx < n else len(upper[0])
    new_field = [[0]*col for _ in range(r)]
    for i in range(len(upper[0])):
        for j in range(len(upper)-1, -1, -1):
            new_field[j][i] = upper[j][i]
    if idx < n:
        new_idx = len(upper[0])
        while idx < n:
            new_field[-1][new_idx] = field[idx]
            idx += 1
            new_idx += 1

    # check 4 direction
    r, c = len(new_field), len(new_field[0])
    copy_field = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            cnt = 0
            for p in range(4):
                nx, ny = i+dx[p], j+dy[p]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or new_field[nx][ny] == 0:
                    continue
                tmp = (new_field[i][j] - new_field[nx][ny]) // 5
                if tmp > 0:
                    cnt += tmp
                    copy_field[nx][ny] += tmp
            copy_field[i][j] += (new_field[i][j] - cnt)

    queue = []
    for i in range(c):
        for j in range(r-1, -1, -1):
            if copy_field[j][i] > 0:
                queue.append(copy_field[j][i])

    queue = [queue[:n//2][::-1], queue[n//2:]]
    new_queue = []
    for j in range(0, n//2, n//4):
        ttmp = []
        for i in range(2):
            tmp = []
            for p in range(j, j+n//4):
                tmp.append(queue[i][p])
            if j == 0:
                tmp = tmp[::-1]
            ttmp.append(tmp)
        if j == 0:
            ttmp = ttmp[::-1]

        new_queue.extend(ttmp)

    r, c = len(new_queue), len(new_queue[0])
    new_field = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            cnt = 0
            for p in range(4):
                nx, ny = i + dx[p], j + dy[p]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                tmp = (new_queue[i][j] - new_queue[nx][ny]) // 5
                if tmp > 0:
                    cnt += tmp
                    new_field[nx][ny] += tmp
            new_field[i][j] += (new_queue[i][j] - cnt)

    real_field = []
    for i in range(c):
        for j in range(r-1, -1, -1):
            real_field.append(new_field[j][i])
    if max(real_field) - min(real_field) <= k:
        break
    time += 1
    field = real_field

print(time)
```