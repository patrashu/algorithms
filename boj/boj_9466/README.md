##  BOJ 9466 (G3)

### https://www.acmicpc.net/problem/9466
### Algorithm: DFS

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs(x):
    global result

    visited[x] = 1
    stacked.append(x)
    next_node = graph[x]

    if visited[next_node]:
        if next_node in stacked:
            result += stacked[stacked.index(next_node):]
        return
    else:
        dfs(next_node)



if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        m = int(input())
        graph = [0] + list(map(int, input().split()))
        visited = [0] * (m+1)
        result = []

        for i in range(1, m+1):
            if not visited[i]:
                stacked = []
                dfs(i)

        print(m - len(result))
```
