##  BOJ 1033 (G2)

### https://www.acmicpc.net/problem/1033

### Algorithm: DFS, Dict, Set


``` python
import sys
from collections import defaultdict
input = sys.stdin.readline

def GCD(a, b):
    return b if a%b==0 else GCD(b, a%b)

def change(a, p, b):
    if (a, p) in visited:
        return

    visited[(a, p)] = True
    ingredient[a] *= p
    for i, _ in graph[a]:
        if i != b:
            change(i, p, a)
    
    
if __name__ == '__main__':
    n = int(input())
    ingredient = defaultdict(int)
    graph = [[]*n for _ in range(n)]
    tmp = []

    for i in range(n):
        ingredient[i] = 1

    for i in range(n-1):
        a, b, p, q = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        tmp.append([a, b, p, q])

    for i in range(n-1):
        a, b, p, q=tmp[i]
        visited={}
        change(a, p, b)
        change(b, q, a)

    g = ingredient[0]
    ans = [*ingredient.values()]

    for i in range(n):
        g = GCD(g, ingredient[i])
    
    for i in range(n):
        ans[i] //= g
    
    print(*ans)

```

* graph를 모두 연결한 후에 진행해야한다.
* 최대 공약수를 구해서 나눠준다.
* 문제를 조금 더 꼼꼼히 봐야겠다.