##  BOJ 1043 (G4)

### https://www.acmicpc.net/problem/1043

### Algorithm: Set, Union_Find
### Trials: 2

Fail Code

``` python
import sys
# sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    known = list(map(int, input().split()))[1:]
    party = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    
    ## All True
    if len(known) == 0:
        print(m)

    else:
        for i in range(m):
            for j in range(1, party[i][0]+1):
                if party[i][j] in known:
                    known = known + party[i][1:]
                    break
        
        known = list(set(known))
        # print(known)
        
        for i in range(m):
            flag = True
            for j in range(1, party[i][0]+1):
                if party[i][j] in known:
                    flag = False
                    break

            if flag:
                cnt += 1
                
        print(cnt)         
```

### Success Code  

```python
import sys
# sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    known = set(list(map(int, input().split()))[1:])
    parties = []
    cnt = []
    
    
    for _ in range(m):  
        party = set(map(int, input().split()[1:]))
        if party:
            parties.append(party)
            cnt.append(1)
    
    
    for _ in range(m):
        for i, p in enumerate(parties):
            if known & p:
                cnt[i] = 0
                known.update(p)
    
    print(sum(cnt))
```

