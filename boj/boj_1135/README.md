##  BOJ 1135 (G2)

### https://www.acmicpc.net/problem/1135
### Algorithm: Dynamic programming, Toposort


``` python
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    dp = [0] * n
    
    for x in a[1:]:
        dp[x] += 1

    ## leaf node append
    queue = deque()
    for i in range(1, len(a)):
        if dp[i] == 0:
            queue.append([i, 0])
        
    if len(queue) == 0:
        print(0)
    
    else:
        ## reversed toposort
        while queue:
            node, cnt = queue.popleft()
            if node == 0:
                print(cnt)

            nx = a[node]
            tree[nx].append(cnt+1)
            dp[nx] -= 1

            if dp[nx] == 0:
                tree[nx].sort(reverse=True)
                nt = [tree[nx][i] + i for i in range(len(tree[nx]))]
                queue.append([nx, max(nt)])
```


