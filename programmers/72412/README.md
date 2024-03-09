### 프로그래머스 '순위 검색'(레벻 2)

### https://school.programmers.co.kr/learn/courses/30/lessons/72412

### Algorithm: dict

```python
"""
info => 5만 
query => 10만
"""
from collections import deque 

def solution(info, query):
    answer = []
    info_dict = {
        "java": { 
            "backend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }},
            "frontend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }}
        }, 
        "cpp": { 
            "backend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }},
            "frontend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }}
        },
        "python": { 
            "backend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }},
            "frontend": { "junior": { "pizza": [], "chicken" : [] }, "senior": { "pizza": [], "chicken" : [] }}
        }
    }
    
    for condition in info:
        c = condition.split(" ")
        info_dict[c[0]][c[1]][c[2]][c[3]].append(int(c[4]))
        
    for k in info_dict.keys():
        for kk in info_dict[k].keys():
            for kkk in info_dict[k][kk].keys():
                for kkkk in info_dict[k][kk][kkk].keys():
                    info_dict[k][kk][kkk][kkkk].sort()
        
    # query
    for q in query:
        *cond, score = q.split(" ")
        cond = list(filter(lambda x: x != "and", cond))
        cnt = 0
        dq = deque([(0, [])])
        while dq:
            idx, cmd = dq.popleft()
            if idx == 4:
                score = int(score)
                candits = info_dict[cmd[0]][cmd[1]][cmd[2]][cmd[3]]
                if not candits:
                    continue
                
                left, right = 0, len(candits)-1
                total = right+1
                while left <= right:
                    mid = (left+right)//2
                    if candits[mid] >= score:
                        right = mid - 1
                    else:
                        left = mid + 1

                cnt += total-left
                continue          
                
            if cond[idx] != '-':
                dq.append((idx+1, cmd+[cond[idx]]))
                continue
            if idx == 0:
                for key in info_dict.keys():
                    dq.append((idx+1, cmd + [key]))   
            elif idx == 1:
                for key in info_dict["java"].keys():
                    dq.append((idx+1, cmd + [key]))
            elif idx == 2:
                for key in info_dict["java"]["backend"].keys():
                    dq.append((idx+1, cmd + [key]))
            elif idx == 3:
                for key in info_dict["java"]["backend"]["junior"].keys():
                    dq.append((idx+1, cmd + [key]))

        answer.append(cnt)
    return answer
```
