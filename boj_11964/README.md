# BOJ 11964 (G5)

## https://www.acmicpc.net/problem/11964
### Algorithm: Dynamic Programming, BFS

``` python
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def search():
  global max_cnt
  for i in range(1, t + 1):
    if dp[i]:
      if i + a <= t: dp[i + a] = 1
      if i + b <= t: dp[i + b] = 1
      if max_cnt < i: max_cnt = i


if __name__ == '__main__':
  t, a, b = map(int, input().split())

  dp = [0] * (t + 1)
  max_cnt = 1
  dp[a], dp[b] = 1, 1
  search()
  for i in range(1, t + 1):
    if dp[i]: dp[i // 2] = 1
  search()
  print(max_cnt)
```

### BFS
```python
import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
  t, a, b = map(int, input().split())

  # def queue
  queue = deque([[a, 0], [b, 0]])
  max_cnt = max(a, b)

  # def visited flag
  visited = [0] * (t + 1)
  visited[a], visited[b] = 1, 1

  # run queue
  while queue:
    node, flag = queue.popleft()
    ## when max_cnt == t
    if node == t:
      break

    for next in [a, b]:
      tmp = node + next
      if tmp <= t and not visited[tmp]:
        visited[tmp] = 1
        max_cnt = max(max_cnt, tmp)
        queue.append((tmp, flag))

      if flag == 0 and not visited[node // 2]:
        queue.append((node // 2, 1))

  print(max_cnt)

```