## BOJ 1238 (G3)

### https://www.acmicpc.net/problem/1238

### Algorithm: Graph theory, Dijkstra

#### Trial: 4 (Out of Time)

```python
import sys
import heapq
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def dijkstra(s):
    q = []
    dist = [int(1e9)] * (N+1)
    dist[s] = 0
    heapq.heappush(q, (s, 0))

    ## Dijkstra Algorithm
    while q:
        node, cost = heapq.heappop(q)
        if dist[node] < cost:
            continue

        for n_node, n_cost in graph[node]:
            tmp = cost + n_cost

            if dist[n_node] > tmp:
                dist[n_node] = tmp
                heapq.heappush(q, (n_node, tmp))

    return dist



if __name__ == '__main__':
    N, M, X = map(int, input().split())
    graph = [[]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))

    res = [[]]
    root_path = []

    for i in range(1, N+1):
        res.append(dijkstra(i))

    for i in range(1, N+1):
        root_path.append(res[i][X] + res[X][i])

    print(max(root_path))

```
