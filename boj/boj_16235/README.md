##  BOJ 16235 (G3)

### https://www.acmicpc.net/problem/16235
### Algorithm: Dict, Deque

```python 
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


n, m, k = map(int, input().split())
robot = [list(map(int, input().split())) for _ in range(n)]
foods = [[5]*n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def s_s():
    for i in range(n):
        for j in range(n):
            length = len(trees[i][j])
            for k in range(length):
                if foods[i][j] < trees[i][j][k]:
                    for _ in range(k, length):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    foods[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                foods[i][j] += dead_trees[i][j].pop() // 2


def f_w():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for p in range(8):
                        nx, ny = i + dx[p], j + dy[p]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)

            foods[i][j] += robot[i][j]


for _ in range(k):
    s_s()
    f_w()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])

print(ans)
```

``` python (시간 초과)
import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(depth: int, trees: dict):
    if depth == k:
        ans = 0
        for _, value in trees.items():
            ans += len(value)
        print(ans)
        return

    n_trees = dict()
    die_dict = dict()

    # 봄
    for key in trees.keys():
        cx, cy = key
        # 나무가 하나면
        if len(trees[key]) == 1:
            value = trees[key][0]
            if foods[cx][cy] >= value:
                foods[cx][cy] -= value
                n_trees[key] = [value+1]
            else:
                die_dict[key] = [value]
        # 나무가 여러 개면
        else:
            t_tmp = []
            d_tmp = []
            ages = sorted(trees[key])
            # 최대한 담고
            for value in ages:
                if foods[cx][cy] >= value:
                    foods[cx][cy] -= value
                    t_tmp.append(value+1)
                else:
                    d_tmp.append(value)

            if len(t_tmp) > 0:
                n_trees[key] = t_tmp
            if len(d_tmp) > 0:
                die_dict[key] = d_tmp
    # 여름
    for key, values in die_dict.items():
        cx, cy = key
        for value in values:
            foods[cx][cy] += value//2

    tmp = []
    # 가을
    for key, values in n_trees.items():
        cx, cy = key
        for value in values:
            if value % 5 == 0:
                for i in range(8):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        tmp.append([(nx, ny), 1])

    for key, value in tmp:
        if key in n_trees.keys():
            n_trees[key].append(value)
        else:
            n_trees[key] = [value]
    # 겨울
    for i in range(n):
        for j in range(n):
            foods[i][j] += robot[i][j]

    dfs(depth+1, n_trees)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    robot = [list(map(int, input().split())) for _ in range(n)]
    foods = [[5]*n for _ in range(n)]
    tree_dict = dict()

    # dictionary에 (r,c) 별로 나무 개수 구하기
    for _ in range(m):
        r, c, age = map(int, input().split())
        tree_dict[(r - 1, c - 1)] = [age]

    dfs(0, tree_dict)
```