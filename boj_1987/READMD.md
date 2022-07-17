##  BOJ 1987 (G4)

### https://www.acmicpc.net/problem/1987
### Algorithm: DFS, BFS, Set, Backtracking 


BFS (pass)
```python
import sys
# sys.stdin = open('input.txt', 'rt')
iuput = sys.stdin.readline


def bfs(x, y):
    global cnt

    while visited_list: 
        x, y, sen = visited_list.pop()
        print(x, y, sen)
        cnt = max(cnt, len(sen))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] not in sen:
                visited_list.add((nx, ny, sen + a[nx][ny]))



if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [input().strip() for _ in range(n)]
    cnt = 0

    dx = [0, 1 ,0, -1]
    dy = [1, 0, -1, 0]

    visited_list = set()
    visited_list.add((0, 0, a[0][0]))

    bfs(0, 0)
    print(cnt)
```

DFS (Error)
```python
import sys
# sys.stdin = open('input.txt', 'rt')
iuput = sys.stdin.readline


def dfs(x, y, length):
    global cnt
    cnt = max(cnt, length)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] not in visited_list:
            visited_list.add(a[nx][ny])
            dfs(nx, ny, length+1)
            visited_list.remove(a[nx][ny])



if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [input().strip() for _ in range(n)]
    cnt = 0

    dx = [0, 1 ,0, -1]
    dy = [1, 0, -1, 0]

    visited_list = set(a[0][0])
    dfs(0, 0, 1)
    print(cnt)

```

