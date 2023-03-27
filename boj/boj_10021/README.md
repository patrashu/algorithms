### Boj 10021 (Gold 3)

### https://www.acmicpc.net/problem/10021

### Algorithm: Mininum Spanning Tree

```python
import sys
import heapq

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


def find_set(c):
  while c != parents[c]:
    c = parents[c]

  return c


if __name__ == '__main__':

  ## input
  n, c = map(int, input().split())
  points = []
  for _ in range(n):
    points.append(list(map(int, input().split())))

  ## heapsort
  heap_list = []
  for i in range(n - 1):
    for j in range(i + 1, n):
      tmp = pow((points[j][0] - points[i][0]), 2) + pow((points[j][1] - points[i][1]), 2)
      if tmp >= c:
        heapq.heappush(heap_list, (tmp, (i, j)))

  ## visited
  parents = [i for i in range(n)]
  dist, cnt = 0, 0

  while heap_list:
    cost, (n1, n2) = heapq.heappop(heap_list)
    if find_set(n1) != find_set(n2):
      parents[find_set(n2)] = parents[n1]
      dist += cost
      cnt += 1

      if cnt >= n - 1:
        break

  print(dist if cnt >= n - 1 else -1)

```

#### 실패 원인

- 최소 스패닝 트리 및 heapq list 정렬까지 ok
- Prim 알고리즘과 Kruscal 알고리즘 혼동
- heapq_list 정렬 시에 바로 크루스칼로 접근했어야 했으나, Prim으로 구현하여 에러
- 최소 스패닝 트리가 존재하지 않는 경우 고려 x
