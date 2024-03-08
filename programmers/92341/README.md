### 프로그래머스 '주차 요금 계산' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/92341

### Algorithm: Dict


```python
""" 입출차 요금 계산

입차 / 출차 기록이 주어김
입차만 있으면 23:59에 출차한걸로 간주
누적 주차요금을 일괄 정산 (또들어올수도 있는거)
기본시간 미만 => 기본요금
기본시간 이상 => 기본 + 단위요금(올림)

"""
import math
from collections import defaultdict

def convert(time):
    h, m = time.split(":")
    return int(h)*60 + int(m)

def solution(fees, records):
    res = []
    answer = defaultdict(int)
    basetime, basefee, ticktime, tickfee = fees
    timestamp = defaultdict(int)
    
    for record in records:
        time, num, status = record.split()
        time = convert(time)
        if status == 'IN':
            timestamp[num] = time
        else:
            answer[num] += time - timestamp[num]
            del timestamp[num]
            
    # 출차하지 않은 차가 있으면
    for key, value in timestamp.items():
        time = convert("23:59")
        answer[key] += (time-value)
    
    # 누적 시간요금 계산
    for key, totaltime in sorted(answer.items(), key=lambda x: int(x[0])):
        totalfee = basefee
        if totaltime > basetime:
            totaltime -= basetime # 기본 시간 빼고
            totalfee += math.ceil(totaltime/ticktime) * tickfee
        res.append(totalfee)

    return res
```