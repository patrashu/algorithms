##  BOJ 1005 (G3)

### https://www.acmicpc.net/problem/1005

### Algorithm: Dynamic programming, Toposort


``` python
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

if __name__ == '__main__':
    t=int(sys.stdin.readline())
    
    for _ in range(t):
        n, k = map(int,sys.stdin.readline().split())
        time = [0]+list(map(int,sys.stdin.readline().split()))
        graph = [[] for _ in range(n+1)]

        topo=[0 for _ in range(n+1)]
        dp=[0 for _ in range(n+1)]
    
        for _ in range(k):
            a,b=map(int,sys.stdin.readline().split())
            graph[a].append(b)
            topo[b]+=1
    
        q = deque()
        for i in range(1,n+1):
            if topo[i]==0:
                q.append(i)
                dp[i]=time[i]
    
        while q:
            a=q.popleft()
            for i in graph[a]:
                topo[i]-=1

                dp[i]=max(dp[a]+time[i],dp[i])
                if topo[i]==0:
                    q.append(i)
    
    
        ans=int(sys.stdin.readline())
        print(dp[ans])
```

