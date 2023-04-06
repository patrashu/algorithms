##  BOJ 21608 (G5)

### https://www.acmicpc.net/problem/21608
### Algorithm: Implementation, Brute Force


``` python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    orders = [list(map(int, input().split())) for _ in range(n**2)]
    field = [[0]*n for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = 0
    ans_q = []

    for idx, order in enumerate(orders):
        tmp = []
        for i in range(n):
            for j in range(n):
                if field[i][j] == 0:
                    like, zero = 0, 0

                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            if field[nx][ny] in order[1:]:
                                like += 1
                            elif field[nx][ny] == 0:
                                zero += 1
                    tmp.append([like, zero, i, j])

        tmp = sorted(tmp, key=lambda x: (-x[0], -x[1], x[2], x[3]))
        cd = tmp[0]
        field[cd[2]][cd[3]] = order[0]
        ans_q.append((cd[2], cd[3], idx))

    # 만족도 구하기
    for x, y, idx in ans_q:
        order = orders[idx]
        tmp = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if field[nx][ny] in order[1:]:
                    tmp += 1

        if tmp > 0:
            tmp = 10 ** (tmp - 1)
        answer += tmp

    print(answer)
```