## BOJ 2559 (S3)

### https://www.acmicpc.net/problem/2559

### Algorithm: 

```python
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = []
    res.append(sum(a[:m]))

    for i in range(n-m):
        res.append(res[i] - a[i] + a[i+m])
        
    print(max(res))
```
