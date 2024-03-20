### 프로그래머스 '기둥과 보 설치' (레벻 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/60061

### Algorithm: Implementation

```python
def check(st):
    for x, y, a in st:
        if a == 0:
            if x == 0 or (x-1, y, 0) in st or (x, y, 1) in st or (x, y-1, 1) in st:
                pass
            else:
                return False
        else:
            if (x-1, y, 0) in st or (x-1, y+1, 0) in st or (x, y-1, 1) in st and (x, y+1, 1) in st:
                pass
            else:
                return False
    return True

def solution(n, build_frame):
    st = set()
    
    for y, x, a, b in build_frame:
        if b == 1:
            st.add((x, y, a))
            if not check(st):
                st.discard((x, y, a))
            pass
        else:
            st.discard((x, y, a))
            if not check(st):
                st.add((x, y, a))
            pass
    
    st = sorted(st, key=lambda x: (x[1], x[0], x[2]))
    st = [[k[1], k[0], k[2]] for k in st]
    return st
```
