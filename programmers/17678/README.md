### 프로그래머스 셔틀버스 (레벨 3)

### https://school.programmers.co.kr/learn/courses/30/lessons/17678
### Algorithm: Implementation

```python
"""
09:00부터 n회 t분 간격으로 역에 도착, 최대 m명 탑승 가능
콘이 셔틀타고 사무실로 갈 수 있는 도착시간 중 가장 늦은 시간 (셔틀 막차를 타라)
도착하면 대기열 맨 뒤에 섬
23:59에 집에 감
운행 횟수, 셔틀 운행간격, 최대 인원수, timetable => input
"""
from collections import Counter

def convert(time):
    h, m = time.split(":")
    return int(h)*60 + int(m)

def solution(n, t, m, timetable):
    answer = -1
    timetable = sorted([convert(k) for k in timetable])
    st = 540
    
    # 버스 1대 전까지 처리 가능한 버스 삭제
    for i in range(n-1):
        cnt = min(m, len(list(filter(lambda x: x <= st, timetable))))
        timetable = timetable[cnt:]
        st += t
    
    # 버스 1대일 때 가장 늦게탈 수 있는 시간 구하기
    et = st+t-1
    timetable = list(filter(lambda x: x <= et, timetable))
    
    if len(timetable) >= m:
        if min(timetable) > 540:
            answer = min(timetable[m-1]-1, st-1) # 셔틀 시작했는데, 맨 마지막으로 타야하는 경우
        else:
            answer = timetable[m-1]-1 # 시작 전에 줄이 꽉찬 case
    else:
        answer = st # 맨 마지막 셔틀의 경우 
    
    # 포맷 변환
    h, m = answer//60, answer%60
    h, m = str(h).zfill(2), str(m).zfill(2)
    return h+":"+m
```
