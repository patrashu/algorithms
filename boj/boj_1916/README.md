##  BOJ 1916 (G5)

### https://www.acmicpc.net/problem/1916

### Algorithm: Dijkstra


``` python
import sys
from collections import defaultdict, deque
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def main(n, spt, ept, graph):
  dist = [sys.maxsize]*(n+1)
  dist[spt] = 0
  dq = deque([(spt, 0)]) # pt, cost

  while dq:
    cnode, ccost = dq.popleft()
    # 최단 거리가 아닐 경우 Cut
    if dist[cnode] < ccost:
      continue

    for nnode, ncost in graph[cnode]:
      tmp = ccost + ncost
      if dist[nnode] > tmp:
        dist[nnode] = tmp
        dq.append((nnode, tmp))

  print(dist[ept])


if __name__ == '__main__':
  n = int(input())
  m = int(input())
  graph = defaultdict(list)

  for _ in range(m):
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))

  spt, ept = map(int, input().split())
  main(n, spt, ept, graph)
```