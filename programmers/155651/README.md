### 프로그래머스  '호텔 대실' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/155651

### Implementation


```python (Implementation)
def convert(time):
    h, m = time.split(":")
    return int(h)*60+int(m)


def solution(book_time):
    book_time = [[convert(p[0]), convert(p[1])+10] for p in book_time]
    book_time.sort(key = lambda x: (x[0], x[1]))
    q = []
    
    for s_time, e_time in book_time:
        # 없으면
        if not q:
            q.append(e_time)
            continue
            
        # 있으면 탐색
        # 가장 차이가 적은 곳에 넣는게 유리하려나?
        candit = []
        for i in range(len(q)):
            if q[i] <= s_time:
                candit.append((s_time-q[i], i))
        
        if not candit:
            q.append(e_time)
            continue
        candit.sort(key=lambda x: x[0])
        q[candit[0][1]] = e_time

    return len(q)
```
