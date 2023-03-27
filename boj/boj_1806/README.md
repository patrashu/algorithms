##  BOJ 1806 (G4)

### https://www.acmicpc.net/problem/1806
### Algorithm: Two pointer


``` python
import sys
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline


if __name__ == '__main__':
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    if sum(a) < m:
        print(0)
    else:
        i, j = 0, 0
        num = a[i]
        line = 1e9

        while i <= j:
            if num >= m:
                line = min(line, j-i+1)
                num -= a[i]
                i += 1
            else:
                if j != n-1:
                    j += 1
                    num += a[j]
                else:
                    num -= a[i]
                    i += 1

        print(line)
        
```


