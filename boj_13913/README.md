# BOJ 13913 (G4)

## https://www.acmicpc.net/problem/13913
### Algorithm: BFS, Dynamic Programming


#### Fail Code
``` python
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())

    dp = [None] * 100001
    dp[n] = []

    queue = deque()
    queue.append((n, 0))

    while queue:
        node, cnt = queue.popleft()

        sub = [node - 1, node + 1, node * 2]
        for i in range(3):
            if i <= sub[i] < 100001:
                if sub[i] == m:
                    print(cnt + 1)
                    ans = dp[node] + [node] + [m]

                    for num in ans:
                        print(num, end=' ')
                    sys.exit(0)

                else:
                    if dp[sub[i]] is None:
                        dp[sub[i]] = dp[node] + [node]
                        queue.append((sub[i], cnt + 1))

                    else:
                        if len(dp[sub[i]]) > len(dp[node]):
                            dp[sub[i]] = dp[node] + [node]
                            queue.append((sub[i], cnt + 1))

```

#### Success Code
```python
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())

    dp = [0] * 100001
    visited = [0] * 100001

    queue = deque()
    queue.append(n)

    while queue:
        node = queue.popleft()
        if node == m:
            print(visited[node])
            ans = []

            while node != n:
                ans.append(node)
                node = dp[node]
            ans.append(n)
            ans.reverse()
            print(' '.join(map(str, ans)))
            break

        for next in (node - 1, node + 1, node * 2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[node] + 1
                queue.append(next)
                dp[next] = node

```
