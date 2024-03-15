### 프로그래머스 방금그곡 (레벨 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/17683
### Algorithm: Implementation, String, math

```python
import math

def convert(time):
    h, m = time.split(":")
    return int(h)*60 + int(m)

def preprocess(record):
    record = record.replace("C#", "P")
    record = record.replace("D#", "Q")
    record = record.replace("F#", "R")
    record = record.replace("G#", "S")
    record = record.replace("A#", "W")
    record = record.replace("B#", "X")  # ?
    return record
    

def solution(m, musicinfos):
    answer = [] # 재생 시간, 입력 순서, 노래 이름
    m = preprocess(m)
    
    for i, info in enumerate(musicinfos):
        st, et, mname, record = info.split(",")
        runtime = convert(et) - convert(st)
        record = preprocess(record)
        melody = None
        
        # 멜로디 반복
        if runtime > len(record):
            record = record * (math.ceil(runtime / len(record)))
        melody = record[:runtime]
        
        # 체크
        if m in melody:
            answer.append((runtime, i, mname))
            
    answer.sort(key=lambda x: (-x[0], x[1]))
    return "(None)" if not answer else answer[0][2]
```
