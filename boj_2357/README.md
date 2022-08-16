# BOJ 2357 (G1)

## https://www.acmicpc.net/problem/2357

### Algorithm: SegmentTree

``` python
import sys
sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

def min_init(start, end, idx):
    if start == end:
        min_tree[idx] = arr[start-1]
        return min_tree[idx]
    
    mid = (start+end)//2
    min_tree[idx] = min(min_init(start, mid, idx*2), min_init(mid+1, end, idx*2+1))
    return min_tree[idx]

def max_init(start, end, idx):
    if start == end:
        max_tree[idx] = arr[start-1]
        return max_tree[idx]
    
    mid = (start+end)//2
    max_tree[idx] = max(max_init(start, mid, idx*2), max_init(mid+1, end, idx*2+1))
    return max_tree[idx]

def min_find(start, end, idx, left, right):
    if left > end or right < start:
        return 1e9
    
    if right >= end and left <= start:
        return min_tree[idx]
    
    mid = (start+end)//2
    tmp = min(min_find(start, mid, idx*2, left, right), min_find(mid+1, end, idx*2+1, left, right))
    return tmp

def max_find(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    
    if right >= end and left <= start:
        return max_tree[idx]
    
    mid = (start+end)//2
    tmp = max(max_find(start, mid, idx*2, left, right), max_find(mid+1, end, idx*2+1, left, right))
    return tmp
      
      
if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    min_tree = [0]*(n*4)
    max_tree = [0]*(n*4)
    
    for _ in range(n):
        arr.append(int(input()))
    
    min_init(1, n, 1)
    max_init(1, n, 1)

    for _ in range(m):
        p, q = map(int, input().split())
        print(min_find(1, n, 1, p, q), end=' ')
        print(max_find(1, n, 1, p, q))
        
```
