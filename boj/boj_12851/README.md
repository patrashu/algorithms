# BOJ 12851 (G4)

## https://www.acmicpc.net/problem/12851
### Algorithm: BFS

``` python
import sys
#sys.stdin = open("input.txt", "r")
from collections import deque


def main(n, k):
  dq = deque([(n, 0)])  # cur_pos, cnt_move
  visited = [sys.maxsize] * 100001
  visited[n] = 0
  min_move_cnt, cnt_way = sys.maxsize, 0  # init to (max, 0)

  while dq:
    cur_pos, cnt_move = dq.popleft()
    if cnt_move >= min_move_cnt:
      continue

    for npt in [cur_pos + 1, cur_pos - 1, cur_pos * 2]:
      if npt < 0 or npt > 100000 or visited[npt] < cnt_move + 1:
        continue

      visited[npt] = cnt_move + 1
      dq.append((npt, cnt_move + 1))
      if npt == k:
        min_move_cnt = visited[npt]
        cnt_way += 1

  # same
  if cnt_way == 0:
    min_move_cnt, cnt_way = 0, 1
  print(min_move_cnt)
  print(cnt_way)


if __name__ == '__main__':
  n, k = map(int, input().split())
  main(n, k)
```