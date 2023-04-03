### 프로그래머스  '과제 진행하기' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/176962

### 우선순위 큐


```python
from heapq import heappush, heappop

# HH:MM => Minute
def time2min(value):
    tmp = value.split(':')
    return int(tmp[0])*60 + int(tmp[1])

def solution(plans):
    answer = []
    wait_queue = []
    cplans = []
    
    for i in range(len(plans)):
        pn, st, lt = plans[i]
        st = time2min(st)
        lt = int(lt)
        
        heappush(cplans, (st, lt, pn))
    
    # 최소 힙
    while len(cplans) >= 2:
        st, lt, pn = heappop(cplans)
        nst, nlt, npn = heappop(cplans)
        
        # 종료 시간이 다음 실행시간보다 작/같 일 때
        if st + lt <= nst:
            answer.append(pn)
            waste_time = nst - (st + lt)
            
            
            # 시간 남으면 나머지 처리
            while waste_time and wait_queue:
                rst, rlt, rpn = heappop(wait_queue)
                
                if rlt <= waste_time:
                    answer.append(rpn)
                    waste_time -= rlt
                else:
                    heappush(wait_queue, (rst, (rlt-waste_time), rpn))
                    waste_time = 0
                
        # 종료 시간이 다음 실행시간보다 클 때
        else:
            heappush(wait_queue, (-st, lt-(nst-st), pn))
            
        heappush(cplans, (nst, nlt, npn))
        
    last = heappop(cplans)
    answer.append(last[2])
    
    while wait_queue:
        remain = heappop(wait_queue)
        answer.append(remain[2])
        
    return answer
```    