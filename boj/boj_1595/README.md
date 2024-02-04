##  BOJ 1595 (G4)

### https://www.acmicpc.net/problem/1595
### Algorithm: BFS, Tree


``` python
import sys
from collections import deque


graph = [[] for _ in range(10001)]

while True:
    try:
      a, b, c = map(int, input().split())
      graph[a].append([b, c])
      graph[b].append([a, c])
    except:
        break

def bfs(spt):
  dq = deque([(spt, 0)])
  visited = [False for _ in range(10001)]
  visited[spt] = True
  max_dist, target_node = 0, 0
  
  while dq:
    cur_node, dist = dq.popleft()
    for next_node, ndist in graph[cur_node]:
      if not visited[next_node]:
        visited[next_node] = True
        ndist = ndist + dist
        if ndist > max_dist:
          max_dist = ndist
          target_node = next_node
        dq.append([next_node, ndist])
  
  return [max_dist, target_node]

print(bfs(bfs(1)[1])[0])
```

### 트리의 지름을 구하는 방법
- 임의의 노드 (여기서는 1)에서 가장 먼 노드를 찾는다.
- 해당 노드로부터 가장 먼 노드를 찾는다
- 두 노드사이의 경로가 트리의 지름(가장 긴 거리)가 된다.
