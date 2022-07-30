##  BOJ 1112 (G1)

### https://www.acmicpc.net/problem/1112
### Algorithm: Simulation


``` python
def mod(n, b):
    r = n % abs(b)
    if r < 0:
        r += abs(b)
    return r

def base(n, b, a):
    na = abs(n) if b > 0 else n
    t = 0
    c = 0
    while na:
        t = mod(na, b)
        na = (na-t)/b
        a[c] = int(t)
        c += 1
        
    if not c:
        c += 1
        a[c] = 0
        
    return b>0 and n<0

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * 64
    
    base(n, m, a)
    
    i = 0
    for i, num in enumerate(reversed(a)):
        if num != 0:
            break
    i = 64 - i
    a = a[:i]
    
    if n < 0 and m > 0:
        print('-', end='')
    for num in reversed(a[:i]):
        print(num, end='')
```


