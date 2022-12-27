## BOJ 17182 (G3)

### https://www.acmicpc.net/problem/17182

### Algorithm: Floyd wassal, Backtracking

```python
import sys

input = sys.stdin.readline


def backtracking(node, cnt, cost):
  global result

  if cnt == N:
    result = min(result, cost)
    return

  for next in range(N):
    if not visit[next]:
      visit[next] = True
      backtracking(next, cnt + 1, cost + graph[node][next])
      visit[next] = False


if __name__ == '__main__':
  N, K = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(N)]

  ## 플로이드 워셜 알고리즘
  for k in range(N):
    for i in range(N):
      for j in range(N):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

  ## 방문 여부 check
  visit = [False] * N
  result = int(1e9)
  visit[K] = True

  ## 백트랙킹
  backtracking(K, 1, 0)
  print(result)
```

- 플로이드 워셜로 각 노드에서의 최단 거리 구하기
- 백트랙킹을 활용하여 K에서 전체 노드를 탐색하는 가장 최단 cost 찾기
