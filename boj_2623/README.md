## BOJ 2623 (G3)

### https://www.acmicpc.net/problem/2623

### Algorithm: Data Structure(Toposort)

```python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline
from collections import deque


def toposort(q, line):

    while q:
        node = q.popleft()
        result.append(node)

        for edge in a[node]:
            line[edge] -= 1
            if line[edge] == 0:
                q.append(edge)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    line = [0] * (n+1)

    for _ in range(m):
        inp = list(map(int, input().split()))
        for i in range(inp[0]-1):
            a[inp[i+1]].append(inp[i+2])
            line[inp[i+2]] += 1

    q = deque()
    result = []
    for i in range(1, n+1):
        if line[i] == 0:
            q.append(i)

    toposort(q, line)

    if len(result) == n:
        for num in result:
            print(num)
    else:
        print(0)

```
