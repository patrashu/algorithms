## BOJ 1976 (G4)

### https://www.acmicpc.net/problem/1976

### Algorithm: DFS, Union Find

```python
import sys

input = sys.stdin.readline


def dfs(x):
  for i, node in enumerate(graph[x]):
    if node == 1 and not visited[i]:
      visited[i] = 1
      dfs(i)


if __name__ == '__main__':
  n = int(input())
  m = int(input())

  graph = [list(map(int, input().split())) for _ in range(n)]
  trav = list(map(int, input().split()))

  visited = [0] * n
  visited[trav[0] - 1] = 1
  ## 순회
  dfs(trav[0] - 1)

  ## 방문 노드 여부 판단
  flag = True
  for num in trav:
    if visited[num - 1] == 0:
      flag = False
      break

  print("YES" if flag else "NO")
```

- 탐색 할 때 방문하는 노드 정보를 visited 변수에 담아서 처리
- 경로가 어떻든 해당 노드를 갈 수 있으면 경로가 생성될 수 있음
- DFS를 이용하여 visited 변수와 입력 받은 여행 경로를 비교해서 vistied = 0이면 NO, all visited면 YES

```python


import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    while x != parents[x]:
        x = parents[x]
    return x

if __name__ == '__main__':
  n = int(input())
  m = int(input())
  parents = [i for i in range(n)]
  for i in range(n):
      link = list(map(int,input().split()))
      for j in range(n):
          if link[j] == 1:
              union(i,j)

  # 경로 체크
  parents = [-1] + parents
  path = list(map(int,input().split()))
  start = parents[path[0]]
  for i in range(1,m):
      if parents[path[i]] != start:
          print("NO")
          break
  else:
      print("YES")

```
