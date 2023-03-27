### 프로그래머스 2022 카카오 '주차 요금 계산' (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/92341

### Algorithm: Linked List, Set


```python
from collections import defaultdict
import datetime

def solution(fees, records):
    ans = defaultdict(int)
    check = defaultdict(int)
    
    for record in records:
        line = record.split(' ')
        if line[2] == 'IN':
            check[line[1]] = line[0]
        
        else:
            split_in_time = check[line[1]].split(':')
            split_out_time = line[0].split(':')
            
            in_time = datetime.time(int(split_in_time[0]), int(split_in_time[1]))
            out_time = datetime.time(int(split_out_time[0]), int(split_out_time[1]))
            
            hour = out_time.hour - in_time.hour
            minute = out_time.minute - in_time.minute
            
            if minute < 0:
                minute += 60
                hour -= 1
            
            total = hour * 60 + minute
            
            if ans[line[1]] is None:
                ans[line[1]] = total
            else:
                ans[line[1]] += total
                del check[line[1]]
        

    for k in check:
        split_in_time = check[k].split(':')
        in_time = datetime.time(int(split_in_time[0]), int(split_in_time[1]))
        out_time = datetime.time(23, 59)

        hour = out_time.hour - in_time.hour
        minute = out_time.minute - in_time.minute

        if minute < 0:
            minute += 60
            hour -= 1

        total = hour * 60 + minute

        if ans[k] is None:
            ans[k] = total
        else:
            ans[k] += total

            
    res = []
    for k, v in sorted(ans.items(), key=lambda x: x[0]):
        # print(k, v)
        if v <= fees[0]:
            res.append(fees[1])
        else:
            total = v - fees[0]
            res.append(fees[1] + (((total-1)//fees[2])+1) * fees[3])
    
    return res
```
- 해결은 햇으나, 조금 비효율적으로 접근했던것 같다.
- 다음 문제에서는 좀 더 효율적인 접근을 목표로 하자.