### 프로그래머스  '호텔 대실' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/155651

### Implementation, Heapq


```python (Implementation)
def time_to_min(times):
    time = []
    st, et = None, None
    st = times[0].split(":")
    et = times[1].split(":")
    time.append(int(st[0])*60 + int(st[1]))
    time.append(int(et[0])*60 + int(et[1]) + 10)
    return time
    

def solution(book_time):
    new_list = []
    for i in range(len(book_time)):
        new_list.append(time_to_min(book_time[i]))
    
    new_list = sorted(new_list, key=lambda x: (x[0], x[1])) 
    rooms = [new_list[0]]
    cnt = 1
    
    for i in range(1, len(new_list)):
        min_idx = -1
        min_time = 1440
        for j in range(len(rooms)):
            # room의 종료 시점이 다음 시작지점과 같-작 + 최소일 때 갱신
            if rooms[j][1] <= new_list[i][0] and min_time > new_list[i][0]:
                min_idx = j
                min_time = new_list[i][0]
                
        if min_idx == -1:
            rooms.append(new_list[i])
            cnt += 1
        else:
            rooms[min_idx][1] = new_list[i][1]
            
    return cnt
```

```python (Heapq)
from heapq import heappush, heappop

def convert(time):
    h, m = time.split(':')
    return int(h)*60 + int(m)

def solution(book_time):
    q = []
    last_time = [-10]

    for st, et in book_time:
        st, et = convert(st), convert(et)
        heappush(q, (st, et))

    while q:
        n_in, n_out = heappop(q)

        if n_in >= last_time[0]+10:
            heappop(last_time)
            heappush(last_time, n_out)
        else:
            heappush(last_time, n_out)

    return len(last_time)
```