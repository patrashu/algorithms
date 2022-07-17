## BOJ 1922 (G4)

### https://www.acmicpc.net/problem/1922

### Algorithm: Data Structure(Kruskal Algorithm)

```python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


def union(x, y):
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def find(x):
    while parents[x] != x:
        x = parents[x]
    
    return x



if __name__ == '__main__':
    n = int(input())
    m = int(input())
    cost = 0
    cnt = 0

    q = []
    for _ in range(m):
        x, y, dist = map(int, input().split())
        q.append((x, y, dist))

    q = sorted(q, key=lambda x: x[2])
    parents = [x for x in range(n+1)]

    for x, y, dist in q:
        a = find(x)
        b = find(y)
        if a != b:
            union(a, b)
            cost += dist
            cnt += 1

        if cnt >= n-1:
            break

    print(cost)

```
