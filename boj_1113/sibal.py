import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y, tmp):
  global visited, flag, total_cnt

  if x == 0 and y == 0:
    flag = False

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and graph[nx][
        ny] <= tmp and not visited[nx][ny]:
      visited[nx][ny] = 1
      if flag:
        total_cnt += 1

      dfs(nx, ny, tmp)


def check(x):
  global flag
  for i in range(n + 2):
    for j in range(m + 2):
      if graph[i][j] <= x and not visited[i][j]:
        visited[i][j] = 1
        flag = True
        dfs(i, j, x)


if __name__ == '__main__':
  n, m = map(int, input().split())
  ## 입력
  a = [list(input().strip()) for _ in range(n)]
  graph = [[1] * (m + 2) for _ in range(n + 2)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      graph[i][j] = int(a[i - 1][j - 1])

  flag = True
  total_cnt = 0
  for i in range(1, 10):
    visited = [[0] * (m + 2) for _ in range(n + 2)]
    check(i)
    if flag:
      total_cnt += 1

  print(total_cnt)
